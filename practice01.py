name=["harry","sohan","sachin","rahul"]
for items in name:
    if items.startswith("h"):
        print("hello "+items)

i=0
while i<len(name):
    if name[i].startswith("s"):
        print("hello "+str(name[i]))
    i+=1
