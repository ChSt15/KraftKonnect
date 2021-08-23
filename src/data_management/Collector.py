import importlib
import multiprocessing
import time
from time import time_ns

from src.data_management.database.io.DataIO import DataIO
from src.data_management.database.io.KeyIO import KeyIO
from src.data_management.database.io.SetIO import SetIO
from src.data_management.dto.Data import Data
from src.data_management.dto.Source import Source


class Collector:

    def __init__(self, source: Source):
        self.source = source
        # TODO WARNING: change to custom/default accordingly
        script = importlib.import_module('scripts.default.'+self.source.script.rsplit('/')[0])
        self.key_io = KeyIO()
        self.data_io = DataIO()
        self.set_io = SetIO()
        self.set_id = None
        self.key_ids = {key.name: key.id for key in self.key_io.get_all_by_source(self.source.id)}
        self.process = multiprocessing.Process(target=script.run, args=(self.write_data,))
        # TODO Currently always on
        self.start()

    def write_data(self, dictionary):
        try:
            time = dictionary['Time']
        except:
            time = time_ns()
        for key, value in dictionary:
            if value is not None:
                data = Data(self.key_ids[key], time, value)
                self.data_io.insert(data)

    def start(self):
        self.set_id = self.set_io.get_next_set_id()
        self.process.start()

    def stop(self):
        self.process.terminate()