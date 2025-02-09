
# class Variables

class Car:

    total_cars = 0
    def __init__(self,Brand,Model):
        self.__brand = Brand
        self.model = Model
        # self.total_cars += 1
        Car.total_cars += 1



    def get_brand(self): 
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    

    def fuel_type(self):
        return "Gasoline"
    
my_car = Car("Tesla","Model S")
my_car2 = Car("Tesla","Model S")
my_car3 = Car("Tesla","Model S")
print(my_car.total_cars)