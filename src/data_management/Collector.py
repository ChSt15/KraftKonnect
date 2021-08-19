import importlib
import multiprocessing
import time
from time import time_ns

from src.data_management.database.io.DataIO import DataIO
from src.data_management.database.io.SetIO import SetIO
from src.data_management.dto.Data import Data
from src.data_management.dto.Source import Source


class Collector:

    def __init__(self, source: Source):
        self.source = source
        # TODO WARNING: change to custom/default accordingly
        script = importlib.import_module('scripts.default.'+self.source.script)
        self.data_io = DataIO()
        self.set_io = SetIO()
        self.set_id = None
        self.process = multiprocessing.Process(target=script.run, args=(self.write_data,))
        # TODO Currently always on
        self.start()

    def write_data(self, dictionary):
        try:
            timestamp = dictionary['timestamp']
        except:
            timestamp = time.time_ns()
        for key in dictionary:
            print(key)
        data = Data(self.source.id,
                    self.set_id,
                    value,
                    timestamp if timestamp is not None else int(time_ns() / 1000.0 / 1000.0)) # Resolution in ms
        self.data_io.insert(data)

    def start(self):
        self.set_id = self.set_io.get_next_set_id()
        self.process.start()

    def stop(self):
        self.process.terminate()