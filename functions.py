# def print_msg(name="there"):
#     print(type(name))
#     print("hello, ",name)

# name=input("Enter your name: ")
# print_msg("adarsh")
# print_msg(name)

# #passing arguements as a tuple
# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print("average is",sum/len(numbers))
# average(2,3,5,677,6)

# passing arguements as a dictionary
# dict={1:6}
# print(type(dict))
# average(m=3,k=4,t=9)

#passing value as a dictionary
def name(**name):
    print(type(name))
    print(name)
    print("hello, ",name["fname"])
    d="hello, ",name["fname"],"ok"
    return d #it will return dictionary type
print(name(fname="adarsh"))