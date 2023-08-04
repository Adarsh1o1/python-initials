class employe:
  def __init__(self , name, salary):
    self.name=name
    self.salary=salary

  @classmethod #it will handle different formats of string
  def format_string(a, data):
    return a(data.split("-")[0],int(data.split("-")[1]))


e1=employe("adarsh", 12000)
print(e1.name,end=" ")
print(e1.salary)
data="adarsh-12000"
e2=employe.format_string(data)
print(f"{e1.name} {e2.salary}")
