class emp:
  def __init__(self,name):
    self.name=name

class students(emp):
  def __init__(self, name, clas):
    super().__init__(name) # now i can use emp class's any method without writing it again in students class
    self.clas=clas

e1=emp("adarsh")
print(e1.name)
st1=students("harry",5)
print(st1.name, st1.clas)