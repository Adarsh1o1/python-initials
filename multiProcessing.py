import requests,time
import multiprocessing
def f1(name):
    print(f"downloading{name}")
    r=requests.get("https://source.unsplash.com/featured/300x201") 
    open(f"files/{name}.jpg","wb").write(r.content)
    print(f'downloaded{name}')
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
time1= time.perf_counter()
if __name__=="__main__":
    pros = []
    for i in range(50):
        # f1(i)
        p=multiprocessing.Process(target=f1, args=[i])
        p.start()
        pros.append(p)
    for p in pros:
        p.join()
# for i in range(50):
#         f1(i)

time2=time.perf_counter()
print(time2-time1)
