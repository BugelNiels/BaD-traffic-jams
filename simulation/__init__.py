import pyglet
from simulation.highway import Highway
from simulation.simulation import Simulator
import numpy as np
import matplotlib.pyplot as plt
from config import Config

__all__ = ["simulation"]


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
    #print(sim.HW.history)
    x = np.matrix(sim.HW.history)
    print(len(sim.HW.history))
    #plt.ylim(ymin=0)
    plt.plot(x, color='black', linewidth=1)
    plt.show()
    plt.savefig("{}/graph-md-{}.png".format(Config.PLOT_FOLDER, Config.MIN_DISTANCE))

    avgSpeedTable = [sum(i) / len(i) for i in sim.HW.velocityHistory]
    plt.plot(avgSpeedTable, color='black', linewidth=1)
    plt.axhline(y=sum(avgSpeedTable) / len(avgSpeedTable), color='r', linestyle='-')
    plt.show()

    plt.scatter(sim.HW.velocityHistory)
    plt.show()


def spawnSingleCar(df):
    HW.spawnCar(batch)
    if(HW.currentCars >= HW.maxCars):
        pyglet.clock.unschedule(spawnSingleCar)

pyglet.clock.schedule_interval(spawnSingleCar, Config.TICKSPEED*3)
pyglet.clock.schedule_interval(sim.calcNextTick, Config.TICKSPEED)
pyglet.clock.schedule_once(dismiss_sim, dismissDelay)
pyglet.app.run()


