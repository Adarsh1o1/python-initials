import random
str=input("Enter your string to code/decode: ")
words = str.split(" ")

def coder(words):
    new=[]
    for word in words:
        if len(words)>=3:
            random_3letters=["fgs","sdf","rtr","eds","tet","opw"]
            n=len(random_3letters)
            random_letters=random_3letters[random.randint(0,n-1)]
            random_letterss=random_3letters[random.randint(0,n-1)]
            # print(random_letters)
            f_char=word[0]
            word=word[1:]+f_char
            word=random_letters+word+random_letterss
            new.append(word)
        else:
            new.append(word[::-1])
    return new

def decoder(words):
    new=[]
    for word in words:
        if len(words)>=3:
            word=word[3:-3]
            f_char=word[-1]
            word=f_char+word[:-1]
            new.append(word)
        else:
            pass
            # new.append(word[::-1])
    return new

mode=int(input("Choose mode(type 1 for coding and 2 for decoding): "))
if mode==1:
    print("CODING MODE")
    str=" "
    string= str.join(coder(words))
    print(string)
elif(mode==2):
    print("DECODING MODE")
    str=" "
    string= str.join(decoder(words))
    print(string)
else:
    print("Invalid Input")
