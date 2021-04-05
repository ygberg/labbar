a = input('char 1: ')
b = input('char 2: ')

def charprint(a,b):
    a=ord(a)
    b=ord(b)
    while a < b-1:
        print(chr(a+1))
        a+=1
charprint(a,b)