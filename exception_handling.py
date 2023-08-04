# try:
#     a=input("Enter a integer: ")
#     print(f"{int(a)}x 34 is {int(a)*34}")
# except Exception as e:
#     print(e)
# print("some code and end of programm")

def inte(a):
    try:
        print(f"{int(a)}x 34 is {int(a)*34}")
        return 1
    except Exception as e:
        print(e)
        return 0
    #finally keyword is always executed no matter where return is
    finally:
        print("some code and end of programm") 
    

a=input("Enter a integer: ")
print(inte(a))