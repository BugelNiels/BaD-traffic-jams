from pyglet import shapes
import random
import time
from config import Config

class Car:

    def __init__(self, maxSpeed, pos, minDistance, chance, isTokkie):
        self.currentSpeed = Config.START_VELOCITY
        self.maxSpeed = maxSpeed
        self.pos = pos
        self.minDistance = minDistance
        self.nextCar = None
        self.chance = chance
        self.isTokkie = isTokkie

    def setNextCar(self, nextCar):
        self.nextCar = nextCar

    def accelerate(self):
        if(self.nextCar != None and self.nextCar.pos == self.pos):
            print("Crash: ", self.pos)
        #if(self.nextCar != None and self.nextCar.pos - self.pos <= self.minDistance and self.nextCar.pos <= self.currentSpeed + self.pos):
        if(self.nextCar != None and self.nextCar.pos - self.pos <= self.calcMinDistance()):
            return    
        if(self.currentSpeed >= self.maxSpeed):
            return
        self.currentSpeed += 1

    def decelerate(self):
        if(self.nextCar == None):
            return           
        if(self.nextCar.pos > self.currentSpeed + self.pos):
            return
        safeSpeed = max(min(self.nextCar.pos - self.pos - 1, self.currentSpeed), 0)
        if(self.isTokkie):
            tailgateSpeed = max(((self.nextCar.pos + self.nextCar.currentSpeed) - self.pos - self.minDistance), 0)
            self.currentSpeed = tailgateSpeed
            return
        self.currentSpeed = safeSpeed

    def randomize(self):
        if random.random() > self.chance:
            return
        self.brake()
        
    def brake(self, dec=1):
        if(self.currentSpeed == 0):
            return
        self.currentSpeed -= dec
        if(self.currentSpeed < 0):
            self.currentSpeed = 0

    def updatePosition(self):
        self.pos = self.pos + self.currentSpeed

    def initCar(self, batch):
        self.ui = shapes.Rectangle(self.pos, 100, 1, 40, color=(Config.TOKKIE_COLOR if self.isTokkie else Config.NORMAL_COLOR), batch=batch)

    def drawCar(self):
        self.ui.x = self.pos

    def calcMinDistance(self):
        return int(self.minDistance * self.currentSpeed + 1)