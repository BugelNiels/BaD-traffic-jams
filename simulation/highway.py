from .car import Car
import random

minDistance = 20
maxSpeed  = 5

class Highway:

    def __init__(self, maxCars):
        self.maxCars = maxCars

    def spawnCars(self, batch):
        self.cars = [self.spawnCar(batch, i * (maxSpeed + minDistance)) for i in range(self.maxCars)]
        for i in range(self.maxCars):
            j = i + 1
            if(j < self.maxCars):
                self.cars[i].setNextCar(self.cars[j])
            else:
                self.cars[i].setNextCar(None)
        
        self.cars = self.cars[::-1]

    def spawnCar(self, batch, pos):
        car = Car(maxSpeed, pos, minDistance, 0.5)
        car.initCar(batch)
        return car

   
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
            car.accelerate()
            car.decelerate()
            car.randomize()
        self.step4()

    def drawCars(self):
        [car.drawCar() for car in self.cars]