class countdown_iterator():
    def __init__(self,n):
        self.n = n +1
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.n != 0:
            self.n -=1
            return self.n
        else:
            raise StopIteration

iterator = countdown_iterator(100)
for item in iterator:
    print(item, end=" ")