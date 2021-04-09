#arr = [1,2,3,4,5]
#print (sum(arr))
#print (sum(arr[0:4]))
b = '12:05:45AM'
m=b[0:-2]
h = b[-2]
a,b,c =m.split(':')
a = int(a)
if h == 'P' and a !=12:
    a = int(a) 
    a +=12
    print(f'{a}:{b}:{c}')
elif h =='A' and a !=12:
    print(f'{a}:{b}:{c}')
else:
    a = 0
    print(f'{a}:{b}:{c}')


print(h)

