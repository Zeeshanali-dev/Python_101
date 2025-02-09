# isinstance

class Car:
    def __init__(self,Brand,Model):
        self.brand = Brand
        self.model = Model
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_car = Car("Tesla","Model S")
print(my_car.full_name())

my_electric_car = ElectricCar("Tesla","Model S","85kWh")
print(isinstance(my_electric_car,Car))
print(isinstance(my_electric_car,ElectricCar))
print(my_electric_car.full_name())
print(my_electric_car.battery_size)