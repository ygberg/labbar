a=1
b=17
c=30

def add_and_subtract(a,b,c):
    x=a
    y=b
    z=c
    print(x,y,z)
    
    def sum_numbers(x,y,z):
        ss = x+y
        sub = z
        print(ss,sub)
    
        def subtract(ss,sub):
            print(ss-sub)
    
        subtract(ss,sub)
    sum_numbers(x,y,z)
add_and_subtract(a,b,c)
