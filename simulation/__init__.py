import pyglet
import random
from simulation.highway import Highway
from simulation.simulation import Simulator
import numpy as np
import matplotlib.pyplot as plt
from config import Config

__all__ = ["simulation"]

random.seed(Config.SEED)

dismissDelay = Config.TICKSPEED * Config.MAX_TICKS

window = pyglet.window.Window(width=Config.SCREEN_WIDTH, height=Config.SCREEN_HEIGHT)
batch = pyglet.graphics.Batch()

HW = Highway(Config.MAX_CARS)
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
    prop = int(Config.PROPORTION * 10)
    
    x = np.matrix(sim.HW.history)
    x *= 0.5
    
    plt.ylim((50000/2,90000/2))
    plt.plot(x, color='black', linewidth=1)
    plt.gcf()
    plt.savefig("{}/graph-prop-{}.png".format(Config.PLOT_FOLDER, prop))
    plt.xlabel('Time in seconds')
    plt.ylabel('Distance in meters')
    plt.show()

    avgSpeedTable = [((sum(i) / len(i)) * 1.8) for i in sim.HW.velocityHistory]
    plt.plot(avgSpeedTable, color='black', linewidth=1)
    plt.axhline(y=sum(avgSpeedTable) / len(avgSpeedTable), color='r', linestyle='-')
    plt.gcf()
    plt.savefig("{}/avg_speed-prop-{}.png".format(Config.PLOT_FOLDER, prop))
    plt.xlabel('Time in seconds')
    plt.ylabel('Speed in km/h')
    plt.show()


def spawnSingleCar(df):
    #HW.spawnCar(batch)
    #if(HW.currentCars >= HW.maxCars):
    pyglet.clock.unschedule(spawnSingleCar)

pyglet.clock.schedule_interval(spawnSingleCar, Config.TICKSPEED*3)
pyglet.clock.schedule_interval(sim.calcNextTick, Config.TICKSPEED)
pyglet.clock.schedule_once(dismiss_sim, dismissDelay)
pyglet.app.run()


