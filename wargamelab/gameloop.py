from card import *
from deck import *
from hand import *
from player import *
from gamemech import *

def chal_c(player1,player2):
        
    c = player1.cv
    
    c2 = player2.cv
    
    if player1.cardsleft ==0:
        return 'player2 has won the game'
    if player2.cardsleft ==0:
        return 'player1 has won the game'
    if c < c2:
        print('player1')
        deck_count(player1,1)
         
    
    if c > c2:
        print('player2')
        deck_count(player2,1)
        
    else:
        #c = player1.hand.cards[3]
        #c2 = player2.hand.cards[3]
        #if c.value() < c2.value:
        #    deck_count(player1,3)
        #    print('player1')
        #if c.value() > c2.value:
        #    deck_count(player2,3)
        #    print('player2')
             
        def deck_count(winner,i):
        
    
            if winner == player1:
                clist = player1.hand.cards[i:-i]
                player1.hand.cards.append(clist)
                clist = player2.hand.cards[i:-i]
                player1.hand.cards.append(clist)
            if winner == player2:
                clist = player1.hand.cards[i:-i]
                player2.hand.cards.append(clist)
                clist = player2.hand.cards[i:-i]
                player2.hand.cards.append(clist)
            #return player1.new_hand(player1.hand),player2.new_hand(player2.hand)


            
d = Deck()
hand = Hand(d,0)
hand1 = Hand(d,1)
player1 = Player('nisse',hand)
player2 = Player('hult',hand1)
#print (player1.hand.cards[0])
print(player1.cardsleft)
#chal_c(player1,player2)


