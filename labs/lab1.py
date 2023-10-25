zadanie1
x = float(input())
y = float(input())
z = float(input())
import math
a = math.sin((math.fabs(x-1))**1/3) - math.cos((math.fabs(y))**1/4) / 1 + x**1/2 + y**1/5
b = (math.fabs(x - 1))**1/2 + math.tan(y) + z**2 / 3 - (math.log(1 + y))
print (a,b)

zadanie2
import math
def f(x):
    a = -2
    return (math.sqrt(x)) / (math.sqrt(x + a)) + 2/3 * x
x = float(input())
print(f(x))

zadanie3
import math
def f(x):
    return (math.sinh(math.cosh(x))) / (math.log(x + 1, 3))
x = float(input())
print(f(x))

zadanie4
h = float(input())
l = float(input())
k = float(input())
import math
r = math.sqrt(l**2 - h**2)
rd = r * k
print(r,rd)
