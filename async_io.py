import asyncio
import requests
async def f1():
    print("downloading 1")
    r=requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq91kK5XgrVta7WBbXz4mAEw-EC2DvwuzR-J5ZExw_&s") 
    open("wallpaper1.jpg","wb").write(r.content)
    return 'downloaded 1'
async def f2():
    print("downloading 2")
    r=requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq91kK5XgrVta7WBbXz4mAEw-EC2DvwuzR-J5ZExw_&s") 
    open("wallpaper2.jpg","wb").write(r.content)
    return 'downloaded 2'
async def f3():
    print("downloading 3")
    r=requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq91kK5XgrVta7WBbXz4mAEw-EC2DvwuzR-J5ZExw_&s") 
    open("wallpaper3.jpg","wb").write(r.content)
    return 'downloaded 3'
async def main():
    # await f1()
    # await f2()
    # await f3()
    a=await asyncio.gather(f1(),f2(),f3())
    print(a)    

asyncio.run(main())