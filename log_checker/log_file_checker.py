content=True
i=1
with open("C:\\Users\\adars\\Desktop\\python\\log_checker\\log_file.txt") as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():
            print(content)
            print("python is present at line ",end="")
            print(i)
        # else:
        #     print('python is not present')
        i+=1
