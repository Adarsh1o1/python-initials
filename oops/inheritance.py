# #inheritance
# class CSE:
#     def __init__(self,name, roll_no):
#         self.name=name
#         self.roll_no= roll_no
#     def show_details(self):
#         print(f"Name of {self.roll_no} is {self.name}")
    
# s1=CSE("adarsh",25492)
# s2=CSE("kashish",25504)


# s1.show_details()
# s2.show_details()

#types of inheritance
#single inheritance
# class animal:
#     def __init__(self,name,breed,eyeColor) -> None:
#         self.name=name
#         self.breed=breed
#         self.eyeColor=eyeColor
#     def eye_color(self):
#         print(f"{self.name} has {self.eyeColor} eye color.")

# class cat(animal):
#     def __init__(self, name, breed, eyeColor) -> None:
#         super().__init__(name, breed, eyeColor)
#     def eye_color(self):
#         return f"{self.name} has green eye color."
#     def sound(self):
#         print(f"{self.name} makes meow sound")

# a1=animal("dog","hsuky","brown")
# a1.eye_color()
# a2=animal("panda","ashwel","black&white")
# a2.eye_color()
 
# cat1=cat("cat1","breed1","black")
# print(cat1.eye_color())
# cat1.sound()

# multiple inheritance
# class employee:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"{self.name}")

# class singer():
#     def __init__(self, songtype):
#         self.songType=songtype
#     def show(self):
#         print(f"{self.songType}")

# class singerEmp(employee,singer):
#     def __init__(self, name,songtype):
#         self.name=name
#         self.songType=songtype

# p1=employee("adarsh")
# p1.show()

# p2=singer("hip-hop")
# p2.show()

# p3=singerEmp("xyz","hindi")
# print(p3.name)
# print(p3.songType)
# p3.show()
# print(singerEmp.mro()) #method resolution order

# multilevel inheritance

class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"{self.name}")

class singer(employee):
    def __init__(self,name, songtype):
        employee.__init__(self,name)
        self.songType=songtype
    def show(self):
        employee.show(self)
        print(f"{self.songType}")

class artist(singer):
    def __init__(self, name , songtype , noOfConcert):
        singer.__init__(self,name,songtype)
        self.noOfConcert= noOfConcert
    def showNoOfConcert(self):
        singer.show(self)
        print(f"{self.name} has done {self.noOfConcert} concerts.")
    
a1=artist("adarsh","english",4)
a1.showNoOfConcert()
a3=artist("adarshh","eenglish",54)
a3.showNoOfConcert()
# print(artist.mro())
# a1.show()

#hybrid inheritance is a form of inheritance which made using different types of inheritance. for eg--> a class made by using multilevel or multiple inheritance etc
class parent():
    pass
class child1(parent):
    pass
class son1(child1):
    pass
class child2(parent):
    pass
class grandChild(child1,child2):
    pass

#hierarchical inheritance 
class baseClass:
    pass
class deriverd1(baseClass):
    pass
class deriverd3(deriverd1):
    pass
class deriverd2(baseClass):
    pass
class deriverd4(deriverd2):
    pass
class deriverd5(deriverd2):
    pass

