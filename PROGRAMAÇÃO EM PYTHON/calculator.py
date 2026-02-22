import math


print("""
    ======================
        Area Calculator 
    ======================\n""")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit\n")

shape = int(input("Which shape:\n"))

if shape == 1:
    base = float(input("Base: "))
    height = float(input("Height: "))
    area = (base * height) / 2
    print(f"Area of triangle is {area:.2f}") 
elif shape == 2:
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
    print(f"Area of rectangle is {area:.2f}")
elif shape == 3:
    side = float(input("Side: "))
    area = side ** 2
    print(f"Area of square is {area:.2f}")
elif shape == 4:
    radius = float(input("Radius: "))
    area = math.pi * radius ** 2
    print(f"Area of circle is {area:.2f}")
elif shape == 5:
    print("Goodbye!")
else:
    print("Invalid option.")
    

