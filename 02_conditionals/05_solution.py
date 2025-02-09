weather = input("what is the weather today?").strip().lower()

if weather == "sunny":
    activity ="Go for a walk"
elif weather == "rainy":
    activity ="Read A book"
elif weather == "snowy":
    activity="Go skiing"

print(activity)