class dictionary_iter ():
    def __init__(self,di):
        self.di=di
        self.ditu = [(k, v) for k, v in self.di.items()] 
        print(self.ditu[0])
        self.i = len(self.ditu) 
        self.j = 0

        
    def __iter__ (self):
        return self
            
    def  __next__ (self):
        try:
            if self.j != self.i:
                self.j +=1
                return self.ditu[self.j]
        except Exception:
                raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:print(x)