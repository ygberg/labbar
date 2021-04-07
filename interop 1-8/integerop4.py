x = int(input('how many lines do you want to process: '))
b = 0
while x != 0:
    a = ord(input('char '))
    b = b + a

    x -= 1
print('The sum equals: {} '.format(b)) 
