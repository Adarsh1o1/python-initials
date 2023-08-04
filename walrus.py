a=True
print(a:=False)

l=[1,23,45,53,32]
while(n:= len(l))>0:
    print(l.pop())

# using tradional method
cars=list()
while True:
    car=input("enter your fav cars: ")
    if car=="quit":
        break
    cars.append(car)

print(cars)

#using walrus operator
foods=list()
while (food:=input("enter your fav food: "))!="quit":
    foods.append(food)
print(foods)
