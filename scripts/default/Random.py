import random
import time
from time import sleep


def run(insert):
    while True:
        sleep(0.005)
        insert({'Random Value': random.random(), 'Timestamp': time.time_ns()})
