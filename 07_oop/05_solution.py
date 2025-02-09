# Polymorphism

class Car:
    def __init__(self,Brand,Model):
        self.__brand = Brand
        self.model = Model



    def get_brand(self): 
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    

    def fuel_type(self):
        return "Gasoline"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric charge"


my_electric_car = ElectricCar("Tesla","Model S","85kWh")
print(my_electric_car.fuel_type())
