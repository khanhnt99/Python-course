from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()

car.go()
car.stop()

motorcycle.go()
motorcycle.stop()