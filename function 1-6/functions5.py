pw = input('type password must be 6 to 10 char long only number and letters: ')

def pwcheck(pw):
    
    pwc = 0
    ints = 0

    if len(pw) > 10 or len(pw) < 6:
        print('password must be between 6 and 10 letters')
    
    else:
        for i in pw:
            
            if i.isdigit():
                ints +=1

            elif ord(i) >= 48 and ord(i) <= 58 or ord(i) >= 65 and ord (i) <=90 or ord(i) >= 97 and ord (i) <=122:
                pwc +=1
                        
            else:
                pwc -=1
                print('password must consist of only letter and digits')
                
            

    if ints >= 2 and pwc+ints == len(pw):
        print(pwc)
        print('password is valid')

    elif ints <2: 
        print('password must contain atlest 2 digits')
       
       


pwcheck(pw) 

