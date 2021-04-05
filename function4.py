s = input('typenumber: ')

def sums_numb(s):
    evensum = 0
    oddsum = 0
    for i in s:
        
        if int(i) % 2 == 0:
            evensum +=int(i)
            
        else:
            oddsum +=int(i)
    print('Odd sum = {}, Even sum = {}'.format(oddsum,evensum))
            
        

sums_numb(s)