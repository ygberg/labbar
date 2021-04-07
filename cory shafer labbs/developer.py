from employee import *

class Developer(Employee):

    raise_amt = 1.04

    def __init__(self,self, first:str, last:str, pay:int, prog_lang:str):
        super().__init__(first:str, last:str, pay:int)
        self.prog_lang = prog_lang
        