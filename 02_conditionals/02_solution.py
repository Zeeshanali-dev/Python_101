age = int(input("Enter your age: "))
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2
else:
    price

print(f"Your ticket price is ${price}")