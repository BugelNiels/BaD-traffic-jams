from .car import Car
import random

minDistance = 6

class Highway:

    def __init__(self, maxCars):
        self.maxCars = maxCars

    def spawnCars(self, batch):
        self.cars = [self.spawnCar(batch, 2 * i * (minDistance + 1)) for i in range(self.maxCars)]
        for i in range(self.maxCars):
            j = i + 1
            if(j < self.maxCars):
                self.cars[i].setNextCar(self.cars[j])
            else:
                self.cars[i].setNextCar(None)

    def spawnCar(self, batch, pos):
        car = Car(5, pos, minDistance, 0.5)
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

    def drawCars(self):
        [car.drawCar() for car in self.cars]