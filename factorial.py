num=int(input("Enter a number: "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

def factorial(x):
    a=1
    for b in range(x):
        a*=b+1
    return a

f=factorial(num)
print(f)

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
    
print(fact(num))