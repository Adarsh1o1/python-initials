with open("twinkle.txt","r") as f:
    data=f.read()
print(data)
if "twinkle" in data:
    print("twinkle is present")
else:
    print("not present")
