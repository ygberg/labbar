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


    