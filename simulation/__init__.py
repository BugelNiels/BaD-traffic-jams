import pyglet
from simulation.highway import Highway
from simulation.simulation import Simulator

__all__ = ["simulation"]

width, height = 1000, 200
window = pyglet.window.Window(width=width, height=height)
batch = pyglet.graphics.Batch()

HW = Highway(20)
sim = Simulator(HW)

HW.spawnCars(batch)


@window.event
def on_draw():
     window.clear()
     HW.drawCars()
     batch.draw()

pyglet.clock.schedule_interval(sim.calcNextTick, 0.1)
pyglet.app.run()


