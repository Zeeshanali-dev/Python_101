class Car:
    def __init__(self,Brand,Model):
        self.brand = Brand
        self.model = Model
    
    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("Tesla","Model S")
print(my_car.full_name())
