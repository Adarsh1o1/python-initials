import time
# print(dir(time))
# in_time=float(time.time())
# for i in range(5000):
#     print(i)
#     time.sleep(1)
# b=float(time.time())-in_time
# in_time=float(time.time())
# i=0
# while(i<5000):
#     print(i)
#     i+=1
# print(b)
# print(float(time.time())-in_time)
while(True):
    t=time.localtime()
    print(time.strftime("%Y.%m.%d %H:%M:%S"))
    time.sleep(1)