# x="hello"
# y=(1,2,3)
# print(dir(x))
# print(dir(y))
class details:
  def __init__(self, name, age):
    self.age=age
    self.name=name

a=details("adarsh", 18)
print(dir(a))
print(a.__dict__)
print(help(a))