from vec import *

class Truck(Vec):

    def __init__ (self,fule,consumtion):
        self.fule = fule 
        self.consumtion = consumtion + 1.6
        
    