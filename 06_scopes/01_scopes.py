username = "zeeshan"

def greet():
    pass

if True:
    pass


x= 99

def f1():
    x=88
    def f2():
        print(x)
        
    return f2
result =f1()
result()

# colousre

def outer(num):
    def inner(x):
        return x ** num
    
    return inner

square = outer(2)

print(square(3))


   

