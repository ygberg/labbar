class Employee():

    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@dakart.com'
    
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay =  self.pay * self.raise_amt