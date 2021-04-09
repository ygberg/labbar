class GameMech ():
    def __init__ (self,player1=None,player2=None):
        self.player1 = player1
        self.player2 = player2
        self.card1 = player1.value
        self.card2 = player2.value
        #self.i = 0
        print(self.card1)
        print(self.card2)
        self.chal_c()

        
        
        

    def chal_c(self):
        print(f"player1's card : {self.card1} player2's card {self.card2}")
        
        if self.player1.cardsleft ==0:
            return 'player2 has won the game'
        if self.player2.cardsleft ==0:
            return 'player1 has won the game'
        if self.card1.value < self.card2.value:
            
            self.deck_count(self.player1,1)
             #self. = 0
        
        if self.card1.value > self.card2.value:
            #self. +=1
            self.deck_count(self.player2,1)
            #self. = 0
        else:
            #c = self.player1.hand.cards[0:3]
            #c2 = self.player2.hand.cards[0:3]
            #if c[2].value() < c2[2].value:
            return print('war')

    def deck_count(self,winner,i):
        
        self.w = winner

        if self.w == self.player1:
            clist = self.player1.hand.cards[i:-i]
            self.player1.hand.cards.append(clist)

            clist = self.player2.hand.cards[i:-i]
            self.player1.hand.cards.append(clist)

        if self.w == self.player2:
            clist = self.player1.hand.cards[i:-i]
            self.player2.hand.cards.append(clist)

            clist = self.player2.hand.cards[i:-i]
            self.player2.hand.cards.append(clist)
        #return player1.new_hand(self.player1.hand),player2.new_hand(self.player2.hand)
       

            