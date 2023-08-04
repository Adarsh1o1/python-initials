# lists
a=[1,2,3,4,23,905,3,978,234,6,7] #lists are created using square brackets[] list can be modified but strings can not
# print(a[0:5]) #slicing a list [from:to(excluded)]
a.append(4)
a.sort()
print(a)
a.reverse()
print(a)
a.append(1002) #adds at the end 
print(a)
a.insert(4,-1) #adds at the given index
print(a)
a.pop(2) #removes element at the given idex
print(a)
a.remove(1002) #removes the provided element
print(a)

#TUPLES

t=(1,2,3,4,5,6,7,8) #it is a tuple CANNOR ASSIGN NEW VALUE or change
print(type(a),type(t))
print(t)
t1=() #empty tuple
print(t1)
t2=(1) 
print(type(t2),t2)
print(t.count(2))
print(t.index(7))
print(sum(t))

# print("practice set")

# f1=input("enter fruit no.1: ")
# f2=input("enter fruit no.2: ")
# f3=input("enter fruit no.3: ")
# f4=input("enter fruit no.4: ")
# f5=input("enter fruit no.5: ")
# f6=input("enter fruit no.6: ")
# f7=input("enter fruit no.7: ")
# fruit_list=[f1,f2,f3,f4,f5,f6,f7]
# # print(fruit_list)

print("dictionary")

dic={"mango":"fruit",
     "adarsh":"coder",
     "lenovo":"brand",
     "numbers":[1,2,4,5],
     "nested_dict":{"my_name":"adarsh"}}
print(dic["numbers"])
print(dic["lenovo"])
print(dic["nested_dict"])
print(dic["nested_dict"]["my_name"])

dic["numbers"]=[7,8]
print(dic["numbers"])

print("dictionary methods")
print(dic.keys()) #returns keys in dictkey type. (type cast it into list)
print(dic.items())
update_dic={
    "keyboard":"input devie",
    "mouse":"input devie",
    "lenovo":"a pc brand" #updates existing key
}
dic.update(update_dic)
print(dic)

#diference between tradional and .get() method
print(dic.get("keyboard1")) #it returns none if key is not present
# print(dic["keyboard1"])

#SETS- it is a collection of non-repetative elements
x={1,23,4,5,7,8} 
print(x)

y={} #this is not a empty set, it is a dictionary type
print(type(y))

#to make a empty set:-
k=set()
print(type(k))
k.add(3)
k.add(2)
k.add(5)
# k.add([1,2,3]) we cannot add list in sets
k.add((1,3,4,4,567,8)) #we can add tuple
#we can only add nonhasable to non-hashable object only
print(k)

#methods of sets

print(len(x))
x.remove(1) #removes the given element
print(x)
x.pop() #removes the arbitirary element
print(x)
z={1,3,5,3,7}
print(x.intersection(z))
print(x.union(z))
print(len(z))
print(type(z))
z.clear()
print(z)
