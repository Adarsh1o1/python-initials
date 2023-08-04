str=input("enter a string: ")
word=input("Enter word to be removed: ")
def string_manipulation(str,word="a"):
    new_str = str.replace(word,"")
    return new_str.strip()

print(string_manipulation(str,word))