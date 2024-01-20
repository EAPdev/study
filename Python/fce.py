#!/usr/bin/env python
import math 


print("a*x^2+b*x+c")
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

d = math.pow(b,2)-4*a*c
X1 = (-b + math.sqrt(d))/(2*a)
X2 = (-b - math.sqrt(d))/(2*a)

print(X1)
print(X2)
