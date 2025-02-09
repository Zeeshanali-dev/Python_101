# fruit Ripness

fruit = input("what is the color of your fruit?").strip().lower()
banana_condition = input("what is the color pf your fruit?").strip().lower()

if fruit == "banana":
    if banana_condition == "green":
        print("Your banana is unripe")
    elif banana_condition == "yellow":
        print("Your banana is ripe")
    else:
        print("Your banana is overripe")
else:
    print("Your Given fruit info is not avilable")