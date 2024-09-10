import math
from math import radians

base=float(input("ingrese la base: "))
altura=float(input("ingrese la altura: "))
angulo=math.radians(float(input("ingrese el angulo: ")))

print(f"superficie del triangulo {(base*altura)/2}")
print(f"base = {base}\nlado 1 = {base*math.sin(angulo)}\nlado 2 = {base*math.cos(angulo)}")