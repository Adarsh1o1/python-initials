num=int(input("Enter a number: "))

def sum_of_natural_no(num):
    if num==1:
        return 1
    else:
        return num+sum_of_natural_no(num-1)
     

print(sum_of_natural_no(num))
 