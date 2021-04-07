num = 50

def loadbar(num):
    num2 = num // 10
    s = '%' * num2
    s2 = '.' * (10-num2)
    if num2 < 10:
        print('{}%'.format(int(num2*10)) + '[' + s +s2+']')
        print('still loading')
    else:
        print('loading complete')
        print('{}%'.format(int(num2*10)) + '[' + s +']')

    
        
loadbar(num)