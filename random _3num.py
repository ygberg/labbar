import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])


loop = 0    #loop variable
i = 0       #loop variable
counter = 0  #counter for right number in right place
near,miss = 0,0
guess=[]
while loop <= 0:
    
    if counter == 0 and loop == 0 and miss == 0 and near == 0:
        n = (input('typ 3 digits'))
        #guess = list(map(int,n.split()))
        
        i,j=0,0
    
    elif counter == 3:
        print('perfect match you have won the game')
        loop += 1

    elif counter != 0 and loop == 0:
        
        print('your guess was {}'.format(n))
        print('you have {} numbers in the right place'.format(counter))
        
        print(' {} nunmbers are in the wrong place'.format(miss))
        n = (input('typ you guess seperate with space: '))
        #guess = list(map(int,n.split()))
       
        i,j = 0,0
        counter,near,miss = 0,0,0
           
    
    while i !=3:
        if digits[i] == int(n[i]):
            counter+=1
            i+=1
        elif digits[i] == int(n[0]) or digits[i] == int(n[1]) or digits[i] == int(n[2])  or miss !=3:
            print('stuck?')
            i+=1
            miss+=1
        else:
            i+=1

       