import pyglet
from pyglet import shapes
from random import randint
from .highway import Highway

class Simulator:
    
    def __init__(self):
        self.HW = Highway(10)
        
    def run(self):
        pass

    def calcNextTick(self):
        self.HW.step1()
        self.HW.step2()
        self.HW.step3()
        self.HW.step4()
        self.updateUI()
        pass

    def initUI(self):
        self.width, self.height = 500, 500
        self.window = pyglet.window.Window(width=self.width, height=self.height)
        self.batch = pyglet.graphics.Batch()

        self.HW.spawnCars(self.batch)
        
        pyglet.app.run()

    @window.event
    def on_draw():
        self.updateUI()

    def updateUI(self):
        self.window.clear()
        self.HW.drawCars()
        self.batch.draw()
