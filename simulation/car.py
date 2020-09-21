from pyglet import shapes

class Car:

    def __init__(self, maxSpeed, pos):
        self.currentSpeed = 0
        self.maxSpeed = maxSpeed
        self.pos = pos

    def accelerate(self):
        pass

    def decelerate(self):
        pass
        
    def updatePosition(self):
        pass

    def initCar(self, batch):
        self.ui = shapes.Rectangle(self.pos*10, 250, 10, 10, color=(255, 255, 255), batch=batch)

    def drawCar(self):
        self.ui.x = self.pos