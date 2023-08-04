# is is equality operator which compares memory loacation/identity
# == operator compares value only

# a=3 # 3 is a constant which is immmutable python does not create new 3 memory
# b=3

# a=(1,2,3,4,5) tuple is also immutable its value can't be changed
# b=(1,2,3,4,5)

# a=[1,2,3,4,5] list's value can be changed it's new m/m location is created even for constant
# b=[1,2,3,4,5]

a= None
b= None

print(a is b)
print(a == b)