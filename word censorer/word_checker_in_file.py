words=["donkey", "mpneky","shit","poo"]
with open("C:\\Users\\adars\\Desktop\\python\\word censorer\\words.txt") as f:
    data=f.read()
for word in words:
    data=data.replace(word,"######")

with open("C:\\Users\\adars\\Desktop\\python\\word censorer\\words.txt","w") as f:
        f.write(data)
        



