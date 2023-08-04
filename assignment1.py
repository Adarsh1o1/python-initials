# Q-1
# x=float(input("Enter first number: "))
# y=float(input("Enter second number: "))
# operator=input("Enter operator: ")
# if operator=="+":
#     print(x+y)
# if operator=="-":
#     print(x-y)
# if operator=="*":
#     print(x*y)
# if operator=="/":
#     print(x/y)
# if operator=="%":
#     print(x%y)

# Q-2" it will become infinite loop 
# n=0
# while n<6:
#     print(n)

# Q-3
# x=55
# x=x+1
# print(x)

# Q-4 storng number is number whose sum factorial of its digit is equal to orignal number
# num=int(input("Enter a number:"))
# def fact(x):
#     fac=1
#     i=1
#     while(i<=x) :
#         fac=fac*i
#         i+=1
#     return fac
# # print(fact(num))
# temp=num
# result=0
# while num>0:
#     m=num%10
#     result=result+fact(m)
#     num//=10
# if temp==result:
#     print(True)

print("Name: shivam \nRoll no. :25517")
# a=int(input("Enter first  number: "))
# b=int(input("Enter second number: "))
# print("\nValue of a before swapping:",a)
# print("Value of b before swapping:",b)
# a=a+b
# b=a-b
# a=a-b
# print("Value of a after swapping:",a)
# print("Value of b after swapping:",b)

# print("Name: Adarsh \nRoll no. :25492")
# print("Name:Shivam\nRoll no.:25517")
# a=int(input("Enter a  number: "))
# if a%2==0:
# 	print(a,"is even")
# else:
# 	print(a,"is odd")
# from math import \

# print("Name:Shivam\nRoll no.:25517")
# num=int(input("Enter a number: "))
# def is_arsmstrong(a):
#     b=len(str(a))
#     # print(len(b))
#     temp=a
#     result=0
#     while temp!=0:
#         m=temp%10
#         # print(m)
#         result+=m**b
#         temp=int(temp/10)
#     return result==a

# if is_arsmstrong(num)==True:
#     print(num,"is a armstrong number")
# else:
#     print(num,"is not a armstrong number")

# print("Name:Shivam\nRoll no.:25517")
# def fibonacci_series(num):
#     a,b=0,1
#     print(a,b,sep=",",end=",")
#     for i in range(2,num):
#         c=a+b
#         print(c,end=",")
#         a,b=b,c
#     return print("")

# num=int(input("Enter number of terms to be printed: "))
# print(fibonacci_series(num))

# def fibonacci_series(num_terms):
#     # Initialize the first two terms
#     a, b = 0, 1
#     # Print the first term
#     print(a)
#     # Print the second term
#     print(b)
#     # Generate the remaining terms
#     for i in range(2, num_terms):
#         # Compute the next term
#         c = a + b
#         # Print the next term
#         print(c)
#         # Update a and b for the next iteration
#         a, b = b, c
# fibonacci_series(10)  # Output: 0 1 1 2 3 5 8 13 21 34
