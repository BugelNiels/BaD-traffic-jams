import pyglet
from pyglet import shapes
from random import randint
from .highway import Highway

class Simulator:
    
    def __init__(self, HW):
        self.HW = HW
        
    def run(self):
        pass

    def calcNextTick(self, dt):
        self.HW.step1()
        self.HW.step2()
        self.HW.step3()
        self.HW.step4()