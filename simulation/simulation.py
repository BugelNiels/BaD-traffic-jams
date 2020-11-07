import pyglet
from pyglet import shapes
from random import randint
from .highway import Highway
from config import Config

class Simulator:

	def __init__(self, HW):
		self.HW = HW
		self.currentTick = 0

	def run(self):
		pass

	def calcNextTick(self, dt):
		if(self.currentTick >= Config.MAX_TICKS - Config.DATA_SIZE):
			self.HW.saveHistory()
		self.HW.allSteps()
		self.currentTick = self.currentTick + 1

