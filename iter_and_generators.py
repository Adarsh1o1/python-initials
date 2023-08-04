list = [1,2,3,4,5,6,7,8,23,435,545]
string = 'hailo'
int = 123
def adarsh_loop(object):
    try:
        iter_list = iter(object)
        while True:
            try:
                print(next(iter_list))
            except:
                break
    except:
        print("object not iterable, f*ck off")
adarsh_loop(list)
adarsh_loop(string)
adarsh_loop(int)



def my_generator():
    for i in range(40+1):
        yield i #it will generate value on the fly when needed

gen=my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in gen:
#     print(i)