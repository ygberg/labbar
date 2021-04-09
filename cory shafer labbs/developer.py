from employee import *

class Developer(Employee):

    raise_amt = 1.04

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
