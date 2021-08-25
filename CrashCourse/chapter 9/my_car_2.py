# import entire module
import car

# note use of modulename.classname, car.Car()
my_car = car.Car("Ford", "Fury", 1965)
print(my_car.get_descriptive_name())

my_electric_car = car.ElectricCar("Tesla", "Model X", 2020)
print(my_electric_car.get_descriptive_name())
