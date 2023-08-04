class students:
    def __init__(self, name, branch, designation):
        self.name=name
        self.branch=branch
        self.designation=designation
    def display(self):
        print(f"name={self.name}")
        print(f"branch={self.branch}")
        print(f"designation={self.designation}")

class staff(students):
    def __init__(self, name, branch, designation):
        super().__init__(name, branch, designation)
    def show(self):
        return super().display()
        
        

a=students("adarsh","ecs","student")
a.name="a"
a.branch="s"
a.designation="c"
# print(students.show(a))
a.display()
b=staff("x","y","z")
b.show()
