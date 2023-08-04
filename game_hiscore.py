score=2

with open("hiscore.txt") as f:
    data=int(f.read())
if data<score:
    with open("hiscore.txt","w") as f1:
        f1.write(str(score))
