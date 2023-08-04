def cube(x):
    return x**3
l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(cube, l)))
print(list(map(lambda x:x*x*x, l)))

#filter funtion
def filterr(a):
    return a>5
print(list(filter(filterr,l)))

from functools import reduce

print(reduce((lambda x,y: x+y),l))