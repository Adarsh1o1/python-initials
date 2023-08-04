class forms:
  # def __init__(self,Name):
  #   self.name= Name
  company="adarsh enterprise"
  def info(self):
    print(f"my name is {self.name} and i own {self.company}")

  # @classmethod #it used to directly chnage class variable
  def change_company(self, new_name):
    self.company=new_name
    
a=forms()
a.name="harry"
a.info()
a.change_company("adarsh's enterprises") #it will only change for 'a' instance
a.info()
b=forms()
b.name="adarsh"
b.info()
f=input()
print(f)