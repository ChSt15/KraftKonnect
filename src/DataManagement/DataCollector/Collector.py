import subprocess
from src.DataManagement.Database.Connection import Connection
from src.DataManagement.IO.DataIO import DataIO
import subprocess
import importlib
from threading import Thread
import multiprocessing
from src.DataManagement.DTO.Source import Source
from src.DataManagement.DTO.Data import Data
from src.DataManagement.IO.SetIO import SetIO
from time import time_ns

class Collector:

    def __init__(self, origin):
        self.origin = origin
        script = importlib.import_module('customScripts.'+self.origin.script)
        self.dataIO = DataIO()
        self.setIO = SetIO()
        self.nextSetId = -1
        self.process = multiprocessing.Process(target=script.run, args=(self.writeData,))

    # Iterate over received data tuple
    # elems may be value or 2-tuple
    # elem: add timestamp
    # tuple: first val is data, snd is tuple
    def writeData(self, *data):
        for source, d in enumerate(data, start=1):
            if type(d) is tuple:
                # data contains time
                dObj = Data(self.setId, source, self.origin.id, d[0], d[1])
                self.dataIO.write(dObj)
            else:
                # Add time if not in data
                timens = time_ns()
                dObj = Data(self.setId, source, self.origin.id, d, timens)
                self.dataIO.write(dObj)


    def start(self):
        self.setId = self.setIO.getNextSetId()
        self.process.start()

    def stop(self):
        self.process.terminate()