from vec import *
from car import *
from truck import *


car1 = Car(20,5)


car1.drive(3)
print(car1.fule)
car1.refule(10)
print(car1.fule)
truck1 = Truck(100, 15)
print(type(truck1))
truck1.drive(5)
print(truck1.fule)
truck1.refule(50)
print(truck1.fule)
