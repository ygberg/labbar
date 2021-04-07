a = int(input('type start of ASCII range: '))
b = int(input('type end of ASCII range: '))
if a < b:
    while a != b:
        print(chr(a))
        a += 1
else :
    while b != a:
        print(chr(b))
        b +=1    