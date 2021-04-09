from random import shuffle

class Card():
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        
    
    def show(self):
        high = {14:'A',13:'K',12:'Q',11:'J'}

        if self.value in high:
           print(f'{high.get(self.value)} {self.suit}')
        else:
            print(f'{self.value} {self.suit}')

    def __str__(self):
        return '{}{}'.format(self.value,self.suit)


    def hidden(self):
        print('##')



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

class Player():
    def __init__(self, name, hand):
        
        self.name = name
        self.hand = hand
    
    def draw(self):
        if len(self.hand) !=0:
            return self.hand[0]
            
    def show_hand(self):
        c=0
        for i in self.hand:
            i.show()        
   
    def won(card,card2):
        hand.append(card1)
        hand.append(card2)       

    def war(self):
        pass


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
                return self.cards,self.count 
        else:
            
            deck2 = self.deck.cards[26:51]
           
            for i in deck2:
                self.cards.append(i)
            return self.cards, self.count 


class GameMech ():
    def __init__ (self,player1=None,player2=None):
        self.player1 = player1
        self.player2 = player2
        self.card1 = player1.hand.cards[0]
        self.card2 = player2.hand.cards[1]
        self.chal_c()

        print(self.card1)
        print(self.card2)
        
        

    def chal_c(self):
    
        if self.card1.value > self.card2.value:
            
            c = self.player1.hand.cards[0]
            self.player1.hand.cards.remove(c)
            self.player1.hand,cards.append(c)
            c = self.player2.hand.cards[0]
            self.player2.hand.cards.remove(c)
            
            self.player1.hand.cards.append(c)
            return print('player1 has won')
        
        if self.card1.value < self.card2.value:
            
            c = self.player1.hand.cards[0]
            self.player1.hand.cards.remove(c)
            
            self.player2.hand.cards.append(c)
            c = self.player2.hand.cards[0]
            self.player2.hand.cards.remove(c)
            
            self.player2.hand.cards.append(c)
            return print('player1 has won'),self.player1,self.player2
        else:
            return print('war')

#hand  = []
#hand2  = []
d = Deck()
h1 = Hand(d,0)
h2 = Hand(d,1)
print(h2.cards[0])
print(h1.cards[0])

p1 = Player('nisse',h1)
p2 = Player('hult',h2)
print(p2.hand.cards[0])
print(p1.hand.cards[0])
tc = p2.hand.cards[0]
tc1 = p1.hand.cards[0]
g = GameMech(p1,p2)
print(p2.hand.cards[0])
print(p1.hand.cards[0])
g1 = GameMech(p1,p2)

#help(h2)
#print(d.cards[0])

#for i in d.cards[0:25]:
#    hand.append(i)
#for i in d.cards[26:51]:
#    hand2.append(i)
#card1 = hand[0]
#card2 = hand2[0]
#p1 = Player('nisse',hand)
#p2 = Player('hult',hand2)
#p1c = p1.draw()
#p2c = p2.draw()
#print(p1c.value)
#print(p2c.value)
#dh = Hand(d,0)
#print(dh.cards[0])




