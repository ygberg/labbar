from deck import *
from card import *

class Hand():

    def __init__ (self,deck,count):
        #super(). __init__()
        self.cards = []
        self.deck = deck
        self.count = count
        self.deal()
   
    def deal (self):
     
        if self.count == 0:
            deck1 = self.deck.cards[0:25]
            for i in deck1:
                #print(i)
                self.cards.append(i)
                
                return self.cards,self.count, print(cards[::])
        else:
            
            deck2 = self.deck.cards[26:51]
           
            for i in deck2:
                self.cards.append(i)
            return self.cards, self.count 
