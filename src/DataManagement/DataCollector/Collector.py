import subprocess
from src.DataManagement.Database.Connection import Connection
from src.DataManagement.Database.IO.DataIO import DataIO
import subprocess

class Collector:

    def __init__(self, sourceId, collectionCode=None):
        self.sourceId = sourceId
        self.dataIO = DataIO()
        self.collectionCode = self.getCode()

    def writeData(self, data):
        self.dataIO.write(data)

    def execute(self):
        sp = subprocess.Popen('test.py')
        for data in iter(sp.)