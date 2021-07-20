import time
from time import sleep
from random import random

provides = ["RandomValueSource1", "RandomValueSource2"]


def run(sendFunc):
    while True:
        sendFunc((time.time_ns(),random()))
        sleep(0.1)