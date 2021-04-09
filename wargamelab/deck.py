from card import *
from random import shuffle
class Deck(Card):
    def __init__(self):
        
        self.cards = []
        self.build_deck()
        self.Shuffel_deck()
        #self.deck1 = self.deck[0:25]
        #self.deck2 = self.deck[26:51]
        
        
    def build_deck(self):
          suit = 'H D S C'.split()
          rank= [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,] 
          
          for i in suit:
              for j in rank:
                #print(i,j)
                self.cards.append(Card(i,j))
    
    def Shuffel_deck(self):
        slist =[]
        for i in range(len(self.cards)):
            slist.append(i)
        shuffle(slist)
       
        for i in slist:    
            c = self.cards[i]
            
            self.cards.remove(c)
            self.cards.append(c)
            #print(c.show())
    
    def __str__ (self):
        for i in self.cards:
            print(i.show())
            
        
    def show_deck(self):
        c=0
        for i in self.cards:
            i.show()
