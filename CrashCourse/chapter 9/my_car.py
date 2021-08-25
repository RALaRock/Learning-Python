# import the car class form the module Car.py
from car import Car, ElectricCar

my_new_car = Car("Ford", "Falcon", 1956)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 21000
my_new_car.read_odometer()

my_tesla = ElectricCar("Tesla", "Model C", 2020)
print(my_tesla.get_descriptive_name())
