import math
from math import sqrt
print("'a, b, c'3개의 값을 입력하시오")
a = int(input("Enter the a:  "))
b = int(input("Enter the b:  "))
c = int(input("Enter the c:  "))

d = math.sqrt(b*b) - (4*a*c)
x1 = (-b+d) / (2 * a)
x2 = (-b-d) / (2 * a)
print(x1, x2)