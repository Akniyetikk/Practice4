ex1
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

ex2
x = abs(-7.25)

print(x)

ex3
x = pow(4, 3)

print(x)

ex4
import math

x = math.sqrt(64)

print(x)

ex5
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

ex6
import math

x = math.pi

print(x)

ex7
import random
a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))

ex8
import random
r1 = random.randint(5, 15)
print(r1)

r2 = random.randint(-10, -2)
print(r2)

ex9
import random

a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))

s = "geeks"
print(random.choice(s))

tup = (1, 2, 3, 4, 5)
print(random.choice(tup))

ex10
import random
a = [1, 2, 3, 4, 5]

random.shuffle(a)
print("After shuffle : ")
print(a)

random.shuffle(a)
print("\nSecond shuffle : ")
print(a)

ex11
import math 
a = math.pi/6
print ("The value of sine of pi/6 is : ", end="") 
print (math.sin(a)) 
print ("The value of cosine of pi/6 is : ", end="") 
print (math.cos(a)) 
print ("The value of tangent of pi/6 is : ", end="") 
print (math.tan(a))

ex12
import math 
print (math.e)
