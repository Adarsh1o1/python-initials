post=input("Provide a Post:\n")
if "harry" in post:
    print("harry is present")
elif "HARRY" in post:
    print("HARRY is present")
elif "Harry" in post:
    print("Harry is present")
else:
    print("harry is not present")