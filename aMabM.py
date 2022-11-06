import math as mt
import matplotlib.pyplot as plt
l1 = float(input('enter luminosity of star'))
r = float(input('enter radius of star'))
f1 = l1/(4*mt.pi*r**2)
f2= 4.4 * 10**6
y = f1/f2
print(mt.floor(mt.log((y,100))))


