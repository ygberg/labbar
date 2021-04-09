from employee import *

class Manager(Employee):

    raise_amt = 1.04

    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def add_emp(seld,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(seld,emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

        