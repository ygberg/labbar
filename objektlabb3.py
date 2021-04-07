class Hero():
    def __init__(self, name:str, health:int):
        
        self.name = name
        self.health = health
        print(f'hero {self.name} was created with {self.health}')
    
    def defend(self, damage):
        self.damage = damage
        self.health -= damage
        print(self.health)
        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeted'
        
    def heal(self,amount):
        print(f'{self.health}before heal')
        self.amount = amount
        self.health +=  amount
        print('heal')
        print(self.health)

hero = Hero('peter',100)
print(hero.defend(50))
print(hero.heal(50))
print(hero.defend(99))
print(hero.defend(1))


    