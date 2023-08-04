def function(a,*args,**kwargs): #all argurments are passed to a funtion as a tuple
    print(a)    #we can also pass normal arguements also
    for b,v in kwargs.items():    
        print(f"{b} is a {v}")
    for i in args:
        # print(type(args))
        print(i)
a=[1,2,3,5,6,7,64,2323,6575] #this list is passed as tuple
b={"adarsh":"coder","baki sab":"fuddu"} #this dictionary is passed as dictionary

function("adarsh",*a,**b)

#normal<*args<**kwargs