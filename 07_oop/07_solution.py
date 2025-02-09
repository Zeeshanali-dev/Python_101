
# # static Mehtod

# class Car:

#     total_cars = 0
#     def __init__(self,Brand,Model):
#         self.__brand = Brand
#         self.model = Model
#         # self.total_cars += 1
#         Car.total_cars += 1

#     @staticmethod
#     def general_discription():
#         return "This is a car"
    
# my_car = Car("Tesla","Model S")

# print(my_car.general_discription())
# print(Car.general_discription())
class MyClass:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_max_value(x, y):
        return max(x, y)

# Create an instance of MyClass
obj = MyClass(10)

print(MyClass.get_max_value(20, 30))  

print(obj.get_max_value(20, 30))