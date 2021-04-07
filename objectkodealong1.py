"""
class sample():
    pass
x = Sample()

print(type(x))

class Dog():
    def __init__(self,breed,name):
            self.breed = breed
            self.name = name
    

sam = Dog(breed='Lab')
fido = Dog(breed='huskie')
"""

"""
class Circle():
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius


    def area(self):
        return self.radius * self.radius*Circle.pi

    def SetRadius(self,radius):
        self.radius = radius
    
    def GetRadius(self):
        return self.radius

c = Circle()
c.SetRadius()
print('Radius is: ', c.GetRadius())
print('Area is: ', c.area())

"""
"""
class Animal():

    def __init__(self):
        print('Animal created')
    
    def WhoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def WhoAmI(self):
        print('Dog')

    def Bark(self):
        print('Woof')

d = Dog()
d.WhoAmI()
d.eat()
d.Bark
"""
class Book():
    def __init__(self, title, author, pages):
        print('A book is created ')
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title:%sAuthor:%s Pages. %s'%(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print('A book is destroyed')

book = Book('Python course','Fredrik', 300)
print(book)
print(len(book))


