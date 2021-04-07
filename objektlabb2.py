class Shop ():
    def __init__(self, name:str, items:list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)
    

shop = Shop('Arys Shop', ['CPU','MB','GFX','RAM','Chassi','GPU'])
print(shop.get_items_count())