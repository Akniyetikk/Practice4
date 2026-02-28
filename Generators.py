ex1
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)

ex2
def fun():
    yield 1            
    yield 2            
    yield 3            

for val in fun(): 
    print(val)

ex3
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)
