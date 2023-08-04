from time import sleep
from functools import lru_cache
@lru_cache(maxsize=None) #it will store results, if repeated in next run it will not compute again
#this concept is called memoise
def Gx(n):
    sleep(2)
    return n*3

print(Gx(23))
print(Gx(24))
print(Gx(25))
print(Gx(26))
print(Gx(22))
print(Gx(24))
print(Gx(23))