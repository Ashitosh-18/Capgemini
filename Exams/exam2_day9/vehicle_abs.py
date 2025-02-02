from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(IVehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine started")

    def stop_engine(self):
        print("Bike engine stopped")

class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine started")

    def stop_engine(self):
        print("Truck engine stopped")

c = Car()
b = Bike()
t = Truck()

c.start_engine()
c.stop_engine()

b.start_engine()
b.stop_engine()

t.start_engine()
t.stop_engine()
