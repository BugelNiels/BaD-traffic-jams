from pyglet import shapes
import random
import time
from config import Config

class Car:

    def __init__(self, maxSpeed, pos, isTokkie):
        self.currentSpeed = Config.START_VELOCITY
        self.maxSpeed = maxSpeed
        self.pos = pos
        self.nextCar = None
        self.chance = Config.CHANCE
        self.isTokkie = isTokkie 
        if(self.isTokkie):
            self.followingDistance = Config.TOKKIE_DISTANCE
        else:
            self.followingDistance = Config.NORMAL_DISTANCE

    def setNextCar(self, nextCar):
        self.nextCar = nextCar


    def updateVelocity(self):        
        if(self.nextCar != None and self.nextCar.pos <= self.getFrontPostion()):
            print("Crash: ", self.currentSpeed)
        if(self.nextCar == None):
            distance = Config.MIN_DISTANCE + 1
        else:
            distance = self.nextCar.pos - self.getFrontPostion()

        if(self.isTokkie and self.nextCar != None and self.nextCar.currentSpeed > self.currentSpeed and distance > self.followingDistance):
            self.currentSpeed = min(self.currentSpeed + Config.ACCELERATION, self.nextCar.currentSpeed, self.maxSpeed)
        elif(distance > Config.MIN_DISTANCE):
            self.accelerate(distance)
        elif(distance < Config.MIN_DISTANCE):
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
        self.currentSpeed = 0

    def randomize(self):
        if random.random() > self.chance:
            return
        self.brake()
        
    def brake(self):
        if(self.currentSpeed == 0):
            return
        self.currentSpeed -= Config.EMERGENCY_DECELERATION
        if(self.currentSpeed < 0):
            self.currentSpeed = 0

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
        return (int(255 - (self.currentSpeed / Config.MAX_SPEED) * 255), int((self.currentSpeed / Config.MAX_SPEED) * 255), 0)