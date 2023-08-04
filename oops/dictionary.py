# for d in dict1,dict2,dict3: dict4.update(d)
# print(dict4)
# print(dict1[4][1])
# x=1
# for key in dict1.keys():
#     print(dict1.keys())
    # if dict1[key]:
        # print(key)
# if x in dict1:
#     print('yes',dict1[x])

# print(dict4.keys())
dict1={1: 10, 2: 20, 3: 30, 4:40, 5: 50, 6: 60}
dict2={3:'three',2:'four'}
dict3={5:'five',6:'six'}
dict4={}
# print(dict1.items())
# print(dict1.keys())

# for i,j in dict1.items():
    # print(i,j)
    # print(dict1[i],dict1[j],)

# for d in dict2,dict3: dict4.update(d)
# print(dict4)

# print(sum(dict1.values()))


# dic={}
# for i in range(1,16):
#     dic.update({i:i*i})

# print(dic.items())
# print(dic)


def tips_map_values(obj, fn):
  ret = {}
  for key in obj.keys():
    ret[key] = fn(obj[key])
  return ret
users = {
  'Owen': { 'user': 'Owen', 'age': 29 },
  'Eddie': { 'user': 'Eddie', 'age': 15 }
}

print(tips_map_values(users, lambda u : u['age'])) # {'Owen': 29, 'Eddie': 15}

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

print(sorted(dict2))
print(1>>10)

thislist = ["kapple", "banana", "cherry"]
thislist.sort()
print(thislist)
print(thislist[-4:-1])

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# print(bin(12))

with open('helo.txt','w+') as file:
  file.write("hellewwwwwwwwwwwwwww\nfeuiwfquiwefuqif")
print(1)

with open('helo.txt','r') as file:
#   for x in file:
    print(file.readlines())

import os
os.rmdir('helo.txt')