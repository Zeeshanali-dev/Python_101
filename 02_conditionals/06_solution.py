distance = int(input("Enter the distance: ").strip())

if distance <3:
    transport = "Walk"
elif distance < 15:
    transport = "Bicycle"
else:
    transport = "Car"

print(f"You should use {transport}")