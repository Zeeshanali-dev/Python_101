# encpsulation

class Car:
    def __init__(self,Brand,Model):
        self.__brand = Brand
        self.model = Model


# it not nessary to write get method we can use what ever we want
    def get_brand(self): 
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
    



my_car = Car("Tesla","Model S")
print(my_car.get_brand())

