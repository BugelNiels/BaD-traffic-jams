from .car import Car

class Highway:

    def __init__(self, maxCars):
        self.maxCars = maxCars

    def spawnCars(self, batch):
        self.cars = [self.spawnCar(batch, i * 2) for i in range(self.maxCars)]
        print(self.cars)

    def spawnCar(self, batch, pos):
        car = Car(5, pos)
        car.initCar(batch)
        return car

   
    def step1(self):
        pass

    def step2(self):
        pass

    def step3(self):
        pass

    def step4(self):
        pass

    def drawCars(self):
        [car.drawCar() for car in self.cars]