# Parent class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# Separate components (Composition)
class Battery:
    def battery_info(self):
        return "This is battery info"

class Engine:
   def Engine_info(self):
        return "This is Engine info"

# Child class using Composition
class ElectricCar(Car,Battery,Engine):
    pass

# Creating instances
my_car = Car("Tesla", "Model S")
print(my_car.full_name())  # Output: Tesla Model S

my_electric_car = ElectricCar("Tesla", "Model S", "85kWh", "1.5L")

