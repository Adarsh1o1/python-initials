class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

    # def __add__(self, v2): #it will return string which is working fine but is not appropriate as i am dealing with vectors
    #     return f"{self.i+.i}i+{self.j+v2.j}j+{self.k+v2.k}k"

    def __add__(self, v2): # so i made this method featuring that it will return vector not a STRING but is not working as expected help me :(
        return vector(self.i-v2.i, self.j+v2.j, self.k+v2.k)

    # def __str__(self):
    #     print("this class is vector")


v1 = vector(1, 2, 3)
print("vector v1 is ",str(v1))
v2 = vector(4, 5, 6)
print("vector v2 is ",str(v2))

print("the sum of v1 and v2 is ",v1+v2)
print("the type of object is ",type(v1+v2))
