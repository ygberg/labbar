tank_Cap = 255
fill_Temp = 0
fill_Times = int(input('filling occation planned 1-20: '))
if  fill_Times <= 20:
    while fill_Times != 0:
        fill_O = int(input('How many Liters do you wanna put in tank 1-1000:'))
   
        if fill_Temp + fill_O > tank_Cap:
            print('Insufficient capacity!')
            break
        else:
             fill_Temp = fill_O + fill_Temp
    fill_Times -= 1
    print('There is ' + str(fill_Temp) + ' Liters in the tank')
else :
    print('input error')
        