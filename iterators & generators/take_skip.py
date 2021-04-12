class Take_Skip ():
    def __init__(self,n,i):
        self.n = n
        self.i = i
        self.j = 0

    def __iter__ (self):
        return self
            
    def  __next__ (self):
        if self.i !=0 :
            self.j += self.n
            self.i-=1
            
            return self.j
        else: 
           raise StopIteration
numbers = Take_Skip(2, 6)
for number in numbers:
    print(number)

numbers = Take_Skip(10, 5)
for number in numbers:
    print(number)
