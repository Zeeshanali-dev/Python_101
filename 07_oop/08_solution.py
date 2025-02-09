
# Decorator

class Car:

    def __init__(self,Brand,Model):
        self.__brand = Brand
        self.__model = Model

    @property
    def model(self):
        return self.__model
        

   
my_car = Car("Tesla","Model S")
# my_car.model = "city"
print(my_car.model) 