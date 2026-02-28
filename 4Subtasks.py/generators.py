task1
def s(n):
    for i in range(1, n + 1):
        yield i * i

n = int(input())
for square in s(n):
   print(square)

task2
n = int(input())
def even(n):
    for i in range(0, n + 1, 2):
        yield i

for ev in even(n):
    if ev != 0:
       print(",", end = "")
    print(ev, end="")

task3
def divisible(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
            
n = int(input())
for d in divisible(n):
    print(d, end=" ")

task4
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = map(int, input().split())
for x in squares(a, b):
    print(x)

task5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for c in countdown(n):
    print(c)
