import math
radius = int(input("Enter the radius: ").strip())

def circle_stat(r):
    area =format(math.pi * r**2, ".2f")
    circumference = format(2 * math.pi * r, ".2f")
    return area, circumference

area, circumference = circle_stat(radius)
print(f"Area: {area}")
print(f"Circumference: {circumference}")