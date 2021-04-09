class Player():
    def __init__(self, name, hand):
        
        self.name = name
        self.hand = hand
        self.value = hand.cards[0]
        self.cv = self.value.value
        self.cardsleft = len(hand.cards)
    
    def new_hand(self,hand):
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
