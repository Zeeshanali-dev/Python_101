user_age = int(input("Enter your age: "))

if user_age < 13:
    print("Child")
elif user_age < 20:
    print("Teenager")
elif user_age < 60:
    print("Adult")
else:
    print("Senior")