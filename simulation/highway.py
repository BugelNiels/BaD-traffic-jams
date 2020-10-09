from .car import Car
import random
import pandas as pd
from config import Config

class Highway:

    def __init__(self, maxCars):
        self.maxCars = maxCars
        self.history = []
        self.currentCars = 0
        self.cars = []

    def spawnCars(self, batch):
        between = int(Config.MAX_SPEED * 2 + Config.NORMAL_DISTANCE)
        [self.spawnCar(batch, int(self.maxCars/2) * between - i * between) for i in range(int(self.maxCars/2))]
        
        # self.cars = self.cars[::-1]

    def spawnCar(self, batch, pos=0):
        if(self.currentCars != 0 and self.cars[-1].pos == 0):
            return
        self.currentCars += 1
        car = Car(Config.MAX_SPEED, pos, Config.MIN_DISTANCE, 0.5, random.choice([False]))
        car.initCar(batch)
        if(self.currentCars != 1):
            car.setNextCar(self.cars[-1])
        self.cars.append(car)

    def getCarPos(self, idx):
        if(idx < self.currentCars):
            return self.cars[idx].pos
        return -1

    def saveHistory(self):
        current = [self.getCarPos(i) for i in range(self.maxCars)]
        self.history.append(current)

    def step1(self):
        [car.accelerate() for car in self.cars]

    def step2(self):
        [car.decelerate() for car in self.cars]

    def step3(self):
        [car.randomize() for car in self.cars]

    def step4(self):
        [car.updatePosition() for car in self.cars]

    def allSteps(self):
        for car in self.cars:
            car.updateVelocity()
            car.randomize()
        self.step4()

    def drawCars(self):
        [car.drawCar() for car in self.cars]
