order_size = "Medium"
extra_shots = False

if extra_shots:
    coffee = order_size + " Coffee with extra shots"
else:
    coffee = order_size + " Coffee"

print(coffee)