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
		self.HW.saveHistory()
		#if(self.currentTick > Config.MAX_TICKS):
			#return
		#self.HW.step1()
		#self.HW.step2()
		#self.HW.step3()
		#self.HW.step4()
		self.HW.allSteps()
		self.currentTick = self.currentTick + 1

