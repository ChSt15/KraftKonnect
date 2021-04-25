from time import sleep
from random import random

values = ['Random Value']

def run(sendFunc):
    while True:
        sendFunc(random(), random())
        sleep(0.1)