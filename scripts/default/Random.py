import random
from time import sleep


def run(insert):
    while True:
        sleep(0.05)
        insert(str(random.random()))