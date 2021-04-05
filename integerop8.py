party_S = int(input('how big is the party?: '))
days_A  = int(input('how many days is the party adventuring?: ')) 
earning = 0
days_B = -1
motday = False
while days_A != days_B:
    
    if days_B % 3 == 0:
        print(days_B)
        motday = True
        earning = earning - 3
    elif days_B % 5 == 0:
        print(days_B)
        if motday == True:
            earning = earning + 18
        else:
            earning = earning + 20
    elif days_B % 10 == 0:
            party_S = - 2
    elif days_B % 15 == 0:
            party_S = + 5
    earning = + 48
    motday = False
    days_B += 1
print(str(party_S) + ' companions received ' + str(earning * party_S) + " each")
        



