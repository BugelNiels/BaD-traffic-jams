from pyglet import shapes
import random
import time
from config import Config

class Car:

    def __init__(self, pos, isTokkie):
        self.currentSpeed = Config.START_VELOCITY
        self.pos = pos
        self.nextCar = None
        self.chance = Config.CHANCE
        self.isTokkie = isTokkie 
        if(self.isTokkie):
            self.maxSpeed = Config.TOKKIE_SPEED
        else:
            self.maxSpeed = Config.MAX_SPEED

    def setNextCar(self, nextCar):
        self.nextCar = nextCar


    def updateVelocity(self):
        # Check if the car crashes
        if(self.nextCar != None and self.nextCar.pos <= self.getFrontPostion() - 1):
            print("Crash: ", self.pos, self.nextCar.pos, self.nextCar.pos - self.pos)
        
        # Make sure the code still works for the first car
        if(self.nextCar == None):
            distance = 9999999
        else:
            distance = self.nextCar.pos - self.getFrontPostion()
        
        # The different cases 1) it is in tailgating distance 2) it is close, but not in tailgating distance, 3) it is far way 4) it is exactly at the correct distance
        if(self.isTokkie and self.nextCar != None and distance > Config.TOKKIE_DISTANCE and distance < self.calcMinDistance()):
           self.currentSpeed = min(self.currentSpeed + Config.ACCELERATION, self.currentSpeed + (distance - Config.TOKKIE_DISTANCE), self.maxSpeed)
        if(distance > self.calcMinDistance()):
            self.accelerate(distance)
        elif(distance < self.calcMinDistance()):
            self.decelerate(distance)
        else:
            self.currentSpeed = min(self.currentSpeed, distance)

    def accelerate(self, distance):
        self.currentSpeed = min(self.currentSpeed + Config.ACCELERATION, distance, self.maxSpeed)

    def decelerate(self, distance):
        if(self.nextCar.currentSpeed == 0):
            self.currentSpeed = max(min(self.currentSpeed, distance - 1), 0)
        else:
            self.currentSpeed = min(self.currentSpeed, distance)

    def randomize(self):
        if random.random() > self.chance:
            return
        self.brake()
        
    def brake(self):
        self.currentSpeed = max(self.currentSpeed - Config.EMERGENCY_DECELERATION, 0)

    def updatePosition(self):
        self.pos = self.pos + self.currentSpeed

    def initCar(self, batch):
        self.ui = shapes.Rectangle(self.pos % Config.SCREEN_WIDTH,  Config.SCREEN_HEIGHT -  (int(self.pos / Config.SCREEN_WIDTH) * Config.CAR_HEIGHT), Config.CAR_SIZE, Config.CAR_HEIGHT, color=self.getColor(), batch=batch)

    def drawCar(self):
        self.ui.x = self.pos % Config.SCREEN_WIDTH
        self.ui.y = Config.SCREEN_HEIGHT -  (int(self.pos / Config.SCREEN_WIDTH) * Config.CAR_HEIGHT)
        self.ui.color = self.getColor()

    def getFrontPostion(self):
        return self.pos + Config.CAR_SIZE

    def getColor(self):
        # Color a car red/green depending on its speed (red for slow; green for fast)
        return (int(255 - (self.currentSpeed / self.maxSpeed) * 255), int((self.currentSpeed / self.maxSpeed) * 255), 0)

    def calcMinDistance(self): 
        # Calculate the minimum distance based on the current speed
        if(self.nextCar == None):
            return Config.MIN_DISTANCE + 1
        return int( self.currentSpeed*Config.REACTION_TIME + (self.currentSpeed * self.currentSpeed) / (2*Config.DECELERATION) - (self.nextCar.currentSpeed * self.nextCar.currentSpeed) / (2*Config.DECELERATION))