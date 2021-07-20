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

    def __init__(self, source: Source):
        self.source = source
        script = importlib.import_module('custom.'+self.source.script)
        self.data_io = DataIO()
        self.set_io = SetIO()
        self.set_id = None
        self.process = multiprocessing.Process(target=script.run, args=(self.writeData,))

    def write_data(self, key: str, value: str, timestamp: int = None):
        self.data_io.write(self.set_id, key, value, timestamp if timestamp != None else int(time_ns()/1000))

    def start(self):
        self.set_id = self.set_io.get_next_set_id()
        self.process.start()

    def stop(self):
        self.process.terminate()