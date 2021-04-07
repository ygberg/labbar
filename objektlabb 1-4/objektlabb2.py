<<<<<<< HEAD
class Shop ():
    def __init__(self, name:str, items:list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)
    

shop = Shop('Arys Shop', ['CPU','MB','GFX','RAM','Chassi','GPU'])
=======
class Shop ():
    def __init__(self, name:str, items:list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)
    

shop = Shop('Arys Shop', ['CPU','MB','GFX','RAM','Chassi','GPU'])
>>>>>>> 83187f189bd2a7b08390ef3c66e7a80b0cc5b1f1
print(shop.get_items_count())