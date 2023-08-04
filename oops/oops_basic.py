# classes and object
# class form:
#     name = "adarsh"
#     roll_no = "25492"
#     branch = "ecs"
#     def intro(self): #self maeans vo object jispe ye method/funtion call kiya gya h
#         print(f"my name is {self.name} and my roll no. is {self.roll_no}. My branch is {self.branch}")

# a= form()
# a.name="adarsh"
# a.roll_no = "25492"
# a.branch = "ECS"
# print(a.name)
# print(a.roll_no)
# print(a.branch)

# b= form()
# b.name="kashish"
# b.roll_no = "25504"
# b.branch = "ECS"
# print(b.name)
# print(b.roll_no)
# print(a.branch)

# a.intro()
# b.intro()

# constructors
# class form:
#     def __init__(self, name, roll_no) -> None:
#         self.name= name
#         self.roll_no = roll_no
#     def info(self):
#         print(f"{self.name}'s roll number is {self.roll_no}")

# a=form("adarsh",25492)
# b=form("kashish",25504)
# a.info()
# b.info()

# decorators

# def decorator(hello):
#     def a():
#         print("good morning")
#         hello() 
#         print("good luck")
#     return a

# # @decorator
# def hello():
#     print("hello world")

# # hello()
# #or
# decorator(hello)()


# def decorator(add):
#     def a(*args,**kwargs):
#         print("good morning")
#         add(*args,**kwargs)
#         print("good luck")
#     return a

# @decorator
# def add(c,d):
#     print(c+d)

# add(1,2)

# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     print(a + b)

# my_function(1,2)

# getters and setters
class myclass:
    def __init__(self, num1, num2):
        self._value = num1
        self._age = num2

    def show(self):
        print(f"num1 is {self._value} and num2 is {self._age}")

    @property  # getter
    def valuex10(self):
        return (self._value + self._age) * 10

    @valuex10.setter  # it will set a new value and it will not behave as a funtion
    def valuex10(self, new_value):
        self._age = new_value + 1

    @staticmethod  # static method helps up to create a method without self key word
    def adarsh(a, b):
        return a + b


a = myclass(19, 18)
b = myclass(37, 34)

a.valuex10 = 100  # setting new value by setters
b.valuex10 = 100  # setting new value by setters
a.show()
b.show()
print(a.valuex10)
print(b.valuex10)
print(a.adarsh(1, 4))  # static method

#class variable and instance variable
class form:
    college_name= "Dce" #class variable
    def __init__(self, name) -> None:
        self.name = name
        self.roll_no = 89

    def info(self):
        print(f"{self.name}'s roll number is {self.roll_no} in {self.college_name}")


a = form("adarsh")
a.roll_no = 24  # here roll_no is instance variable which is associated with a
a.college_name="dceggn"
a.info()
b = form("kashish")
b.roll_no = 45
b.info()
# form.info(b)