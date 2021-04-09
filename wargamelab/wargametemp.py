from random import shuffle


class Card():
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        
    
    def show(self):
        print(f'{self.value} {self.suit}')

    def hidden(self):
        print('##')

    """ def real_value(self):
            
        if self.value == 'A' or 'K' or 'Q' or 'J':
            if self.value == 'A':
                return int(14)
            if self.value == 'K':
                return int(13)
            if self.value == 'Q':
                return int(12)
            if self.value == 'J':
                return int(11)
        else:
            
            print(self.value)  """
            
   


class Deck():
    def __init__(self):
        self.deck = []
        self.build_deck()
        self.Shuffel_deck()
        self.deck1 = self.deck[0:25]
        self.deck2 = self.deck[26:51]
        
        
    def build_deck(self):
          suit = 'H D S C'.split()
          rank= '2 3 4 5 6 7 8 9 10 J Q K A '.split()
          
          for i in suit:
              for j in rank:
                #print(i,j)
                self.deck.append(Card(i,j))
    
    def Shuffel_deck(self):
        slist =[]
        for i in range(len(self.deck)):
            slist.append(i)
        shuffle(slist)
       
        for i in slist:    
            c = self.deck[i]
            
            self.deck.remove(c)
            self.deck.append(c)
            #print(c.show())
            
        
    def show_deck(self):
        c=0
        for i in self.deck:
            i.show()
            c+=1
            print(c)

    """ def deal_deck(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        deck1 = self.deck[0:25]
        deck2 = self.deck[26:51]
        return player1(deck1) , player2(deck2) """
    #def __str__ (self):
        #for i in self.deck:
           # print(i.show())
            

class Player():
    def __init__(self,name,Hand):
        self.name = name
        self.hand = Hand
        
        
    def draw(self):
        if len(self.hand) !=0:
            return self.hand[0]
            
            
            
           
    def won(card,card2):
        hand.append(card1)
        hand.append(card2)       

    def war(self):
        pass

class Hand():

    def __init__ (self,deck):
        self.hand = deck.deck[0:25]
        self.hand1 = deck.deck[26:51]
        self.count = 0
        self.deal()
    def deal (self):
        if self.count ==0:
            self.count +=1
            return self.hand1
        else:
            self.count = 0
            return self.hand






d = Deck()
h1 = Hand(d)
h2 = Hand(d)
p1 = Player(nisse,h1)






