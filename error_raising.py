a=input("Enter number between 1-10: ")
if a=="quit":
    exit
elif(int(a)>=10 or int(a)<=1):
    raise ValueError("bola na 1-9 ke bich me hona chaiye number")