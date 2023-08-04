# from threading import Thread
from time import sleep
# import requests
# def f1():
#     print("downloading 1")
#     r=requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq91kK5XgrVta7WBbXz4mAEw-EC2DvwuzR-J5ZExw_&s") 
#     open("wallpaper1.jpg","wb").write(r.content)
#     return 'downloaded 1'
# def f2():
#     print("downloading 2")
#     r=requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq91kK5XgrVta7WBbXz4mAEw-EC2DvwuzR-J5ZExw_&s") 
#     open("wallpaper2.jpg","wb").write(r.content)
#     return 'downloaded 2'
# def f3():
#     print("downloading 3")
#     r=requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq91kK5XgrVta7WBbXz4mAEw-EC2DvwuzR-J5ZExw_&s") 
#     open("wallpaper3.jpg","wb").write(r.content)
#     return 'downloaded 3'

# time1=time.perf_counter()
# # f1()
# # f2()
# # f3()
# t1=Thread(target=f1)
# t2=Thread(target=f2)
# t3=Thread(target=f3)
# t1.start()
# t2.start()
# t3.start()
# # t1.join()
# # t2.join()
# # t3.join()
# time2=time.perf_counter()
# print(time2-time1)

#concurent futures for threding
from concurrent.futures import ThreadPoolExecutor

def f1(seconds):
    print(f"sleeping for {seconds} seconds")
    sleep(seconds)
    return f"sleep for {seconds}"
def f2(seconds):
    sleep(seconds)
    return f"sleep for {seconds}"
def f3(seconds):
    sleep(seconds)
    return f"sleep for {seconds}"
# with ThreadPoolExecutor(max_workers=3) as exe:
#     future1= exe.submit(f1,4)
#     future2= exe.submit(f2,3)
#     future3= exe.submit(f3,1)
#     print(future1.result())
#     print(future2.result())
#     print(future3.result())

# usind map method
with ThreadPoolExecutor() as exe:
    l=[2,4,3,2]
    results=exe.map(f1,l)
    for result in results:
        print(result)

# obs download