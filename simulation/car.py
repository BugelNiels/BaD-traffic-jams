from pyglet import shapes
import random
import time

class Car:

    def __init__(self, maxSpeed, pos, minDistance, chance):
        self.currentSpeed = 5
        self.maxSpeed = maxSpeed
        self.pos = pos
        self.minDistance = minDistance
        self.nextCar = None
        self.chance = chance

    def setNextCar(self, nextCar):
        self.nextCar = nextCar

    def accelerate(self):
        if(self.nextCar != None and self.nextCar.pos == self.pos):
            print("Crash")
            time.sleep(0.1)
        #if(self.nextCar != None and self.nextCar.pos - self.pos <= self.minDistance and self.nextCar.pos <= self.currentSpeed + self.pos):
        if(self.nextCar != None and self.nextCar.pos - self.pos <= self.minDistance):
            return    
        if(self.currentSpeed >= self.maxSpeed):
            return
        self.currentSpeed += 1

    def decelerate(self):
        if(self.nextCar == None):
            return           
        if(self.nextCar.pos > self.currentSpeed + self.pos):
            return
        safeSpeed = min(self.nextCar.pos - self.pos - 1, self.currentSpeed)
        tailgateSpeed = max((self.nextCar.pos + self.nextCar.currentSpeed) - self.pos - self.minDistance, 0)
        if(safeSpeed >= tailgateSpeed):
            self.currentSpeed  = safeSpeed
        elif(self.nextCar.currentSpeed >= self.currentSpeed):
            self.currentSpeed = tailgateSpeed
        else:
            self.currentSpeed = min(safeSpeed, tailgateSpeed)

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
        self.ui = shapes.Rectangle(self.pos, 100, 1, 40, color=(int(random.random() * 255), int(random.random() * 255), int(random.random() * 255)), batch=batch)

    def drawCar(self):
        self.ui.x = self.pos