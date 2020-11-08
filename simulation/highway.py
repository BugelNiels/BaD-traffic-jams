from .car import Car
import random
import pandas as pd
from config import Config

class Highway:

    def __init__(self, maxCars):
        self.maxCars = maxCars
        self.history = []
        self.velocityHistory = []
        self.currentCars = 0
        self.cars = []

    def spawnCars(self, batch):
        between = int(Config.MAX_SPEED * 2 + Config.MIN_DISTANCE)
        [self.spawnCar(batch, int(self.maxCars) * between - i * between) for i in range(int(self.maxCars))]

    def spawnCar(self, batch, pos=0):
        #check if the next car can be spawned at the position
        if(self.currentCars != 0 and self.cars[-1].pos == 0):
            return
        self.currentCars += 1
        
        #get the correct proportion tokkies in the simulation
        car = Car(pos, random.random() < Config.PROPORTION)
        car.initCar(batch)
        #append next car, for ease of calculation
        if(self.currentCars != 1):
            car.setNextCar(self.cars[-1])
        self.cars.append(car)

    def getCarPos(self, idx):
        if(idx < self.currentCars):
            return self.cars[idx].pos
        return -1

    def getCarVelocity(self, idx):
        if(idx < self.currentCars):
            return self.cars[idx].currentSpeed
        return -1

    def saveHistory(self):
        #save the history for the plots
        current = [self.getCarPos(i) for i in range(self.maxCars)]        
        self.history.append(current)

        current = [self.getCarVelocity(i) for i in range(self.currentCars)]
        self.velocityHistory.append(current)

    def allSteps(self):
        for car in self.cars:
            car.updateVelocity()
            car.randomize()
        # This has to happen after all the new velocities have been calculated
        [car.updatePosition() for car in self.cars]

    def drawCars(self):
        [car.drawCar() for car in self.cars]
