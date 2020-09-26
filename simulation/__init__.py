import pyglet
from simulation.highway import Highway
from simulation.simulation import Simulator
import numpy as np
import matplotlib.pyplot as plt

__all__ = ["simulation"]

tickspeed = 0.01
maxTicks = 1000
dismissDelay = tickspeed * maxTicks

width, height = 2560, 200
window = pyglet.window.Window(width=width, height=height)
batch = pyglet.graphics.Batch()

HW = Highway(1000)
sim = Simulator(HW)

HW.spawnCars(batch)


@window.event
def on_draw():
     window.clear()
     HW.drawCars()
     batch.draw()

def dismiss_sim(df):
    pyglet.clock.unschedule(sim.calcNextTick)
    printGraphs()

def printGraphs():
    #print(sim.HW.history)
    x = np.matrix(sim.HW.history)
    #plt.ylim(ymin=0)
    plt.plot(x)
    plt.show()

def spawnSingleCar(df):
    HW.spawnCar(batch)
    if(HW.currentCars >= HW.maxCars):
        pyglet.clock.unschedule(spawnSingleCar)

pyglet.clock.schedule_interval(spawnSingleCar, tickspeed*3)
pyglet.clock.schedule_interval(sim.calcNextTick, tickspeed)
pyglet.clock.schedule_once(dismiss_sim, dismissDelay)
pyglet.app.run()


