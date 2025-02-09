pet_type = input("Enter the pet type: ").strip().lower()
pet_age = int(input("Enter the pet age: ").strip())

if pet_type == "dog":
    if pet_age < 2:
        print("Puppy")
    else:
        print("Adult Dog")
elif pet_type == "cat":
    if pet_age < 2:
        print("Kitten")
    else:
        print("Adult Cat")
else:
    print("Invalid pet type")