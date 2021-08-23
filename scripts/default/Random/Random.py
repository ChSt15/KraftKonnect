import random
import time
from time import sleep

provides = [('Random Value', 1), ('Random Quaternion', 4)]

def run(insert):
    while True:
        sleep(0.005)
        insert({'Random Value': random.random(),
                'Random Quaternion': (random.random(), random.random(), random.random(), random.random()),
                'Time': time.time_ns()})
