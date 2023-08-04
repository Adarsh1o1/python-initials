# print(5**2)

a= lambda x: x**2+2 #it is mathematically written as f(x)=x^2+2
print(a(11)+90) #print a when x=4

z= lambda x,y,z,g: (x+y+z+g)
print(z(1,2,3,4))
 
def sum(m):
    return m+9

def apply(z,value):
    return z(value)+90

print(apply(sum,11))