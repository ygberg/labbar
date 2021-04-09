class Vec:
    #def __init__(self,fule,consumtion):
    #    self.fule = fule
    #    self.consumtion = consumtion
    #    

        def drive(self,distans):
            print(distans)
            self.fule = self.fule - distans * self.consumtion
            return self.fule
                       
            


        def refule(self,refule):
                
            self.fule += refule
            
            return self.fule