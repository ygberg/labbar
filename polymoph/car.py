from vec import *

class Car(Vec):
    def __init__ (self,fule,consumtion):
        self.fule = fule
        self.consumtion = consumtion + 0.9
        self.tank = fule
    

             
