import math
from math import radians
lado=float(input("ingrese base: "))
hipotenusa=float(input("ingrese hipotenusa: "))
ladox=float(hipotenusa**2-lado**2)**0.5
superficie=float((lado*ladox)/2)
angulo=math.degrees(math.asin(lado/hipotenusa))

print(f"lado restante {ladox}, superficie {superficie}")
print(f"angulo 1 = 90º, angulo 2 = {angulo}º, angulo 3 = {180-90-angulo}º")