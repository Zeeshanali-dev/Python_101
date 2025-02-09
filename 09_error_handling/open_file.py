file = open("youtube.txt", "w")


try:
    file.write("hello world")
except:
    print("something went wrong")
finally:
    file.close()

# new method

with open("youtube.txt", "w") as file:
    file.write("hello world")