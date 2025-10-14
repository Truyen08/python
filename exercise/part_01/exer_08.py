import math

a = float(input("Enter the side length: "))
p = (a * 3) / 2
area = math.sqrt(p * (p - a) * (p - a) * (p - a))
print("Equilateral triangle area:", round(area, 2))
