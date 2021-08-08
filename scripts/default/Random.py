import random
from time import sleep


def run(insert):
    while True:
        sleep(0.1)
        insert(str(random.random()))