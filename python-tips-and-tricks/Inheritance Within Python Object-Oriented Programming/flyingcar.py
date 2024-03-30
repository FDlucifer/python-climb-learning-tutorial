class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print("starting engine")

    def stop(self):
        print("stopping engine")


class Car(Vehicle):
    def drive(self):
        print("Driving")


class Aircraft(Vehicle):
    def fly(self):
        print("Flying")


class FlyingCar(Car, Aircraft):
    pass
