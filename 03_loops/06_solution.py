number = int(input("Enter the number: ").strip())
stopNumber = 1

while number > 0:
    stopNumber *=  number
    number -= 1

print(stopNumber)

