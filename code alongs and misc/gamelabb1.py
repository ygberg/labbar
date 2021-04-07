import random
dig = list(range(10))
random.shuffle(dig)
print(dig[:3])


loop = 0    #loop variable
i = 0       #loop variable
counter = 0  #counter for right number in right place
miss = 0     #
guess=[]
while loop <= 0:
    
    if counter == 0 and loop == 0 and miss == 0:
        n = (input('typ your guess seperate with space: '))
        guess = list(map(int,n.split()))
        
        
    
    elif counter == 3:
        print('perfect match you have won the game')
        loop += 1

    elif counter != 0:
        
        print('your guess was {}'.format(guess))
        print('you have {} numbers in the right place'.format(counter))
        
        print(' {} nunmbers are in the wrong place'.format(miss))
        n = (input('typ you guess seperate with space: '))
        guess = list(map(int,n.split()))
       
        i,j = 0,0
        counter,miss = 0,0
           
    
    while i != 3:
        if dig[i] == guess[i]:
            counter +=1
            i+=1
        elif  dig[i] == guess[0] or dig[i] == guess[2] or dig[i] == guess[1] :
            miss +=1
            i+=1
        else:
            i+=1

       