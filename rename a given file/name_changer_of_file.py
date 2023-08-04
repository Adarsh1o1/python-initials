import os
old_name="sample2.txt"
new_name=input("rename a file: ")
with open(old_name) as f1:
    content=f1.read()
with open(new_name,"w") as f2:
    f2.write(content)
os.remove(old_name)



