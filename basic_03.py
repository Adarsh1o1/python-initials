# a='''pc"s and pc's'''
# print(a)

print("string slicing\n")

# #concatinating two strings
# greeting="GOOD MORNING, "
# name=("Adarsh\n")
# print(greeting+name)

a="qwertyui"
print(a[0+2])
print(a[0:4]) #it excludes last index
print(a[-1]) #it excludes last index
print(a[0:]) #it excludes last index
print(a[-4:-1]) #it excludes last index
print(a[0:9:3]) #it prints every 3nd character
print(a[0:9:2]) #it prints every 2nd character

print("string functions\n")

b="hi hello lithi bird \n \t \\ \'"
print(len(b))
print(b.endswith("bird")) #checks if a sting end with given string
print(b.count("h")) #counts occurance given elements in a string
print(b.capitalize()) #only capitalize first character of a string
print(b.find("l")) #finds the given word and returns the index
print(b.replace("hello","lithi")) #replace old word with given word

c="no on can beat me, i am be the best!  "
print(c.find("  "))
print(len(c))
print(c.replace("  "," "))


d='Dear Harry, This Python course is nice. Thanks!'
print(d.replace("Dear Harry, This Python course is nice. Thanks!",'Dear Harry, \n\tThis Python course is nice. Thanks!'))
 
a=input("name ")
print(a)
