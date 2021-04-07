cards = input('input team and number ex. A-7: ')
cards = cards.upper()
cards = str(set(cards.split()))
#cards = set(cards)
#cards = str(cards)

teamAp = 10
teamBp = 10
i = len(cards)
j = 0


while j != len(cards) : 
                
    if 'A' in cards[j]:
        teamAp -=1
        
    elif 'B' in cards[j]:
        teamBp -=1
    
        
    j +=1    
    
if teamAp <=7 or teamBp <= 7:
    print('team A-'+ str(teamAp) +' team B-'+ str(teamBp) +'\n'+ 'game was terminated'  ) 
else:
    print('team A-'+ str(teamAp) +' team B-'+ str(teamBp) +'\n')

