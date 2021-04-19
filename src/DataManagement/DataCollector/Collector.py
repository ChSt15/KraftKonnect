import subprocess
from src.DataManagement.Database.Connection import Connection
from src.DataManagement.IO.DataIO import DataIO
import subprocess

class Collector:

    def __init__(self, sourceId, collectionCode=None):
        self.sourceId = sourceId
        self.dataIO = DataIO()
        self.collectionCode = self.getCode()

    def writeData(self, data):
        self.dataIO.Insert(data)