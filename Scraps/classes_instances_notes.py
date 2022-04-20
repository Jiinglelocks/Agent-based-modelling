# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 18:50:01 2022

@author: Alex
"""
# a class is a blueprint for creating instances.
# each unique employee created with this class, will be an instance of that class
class Employee:
    #pass
    def __init__(self, first, last, pay):
        self.first = first
        # this is the same as emp_1.first = 'Alex'
        # removes the need for such manual assignments
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        #print('{} {}'.format(emp_1.first, emp_1.last)) # this is how the function would look 

emp_1 = Employee('Alex', 'Camilleri', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1, emp_2)
#print(emp_1.email)
#print(emp_2.email)



print(emp_1.fullname()) # the instance (emp_1) is being passed in automatically, so have to expect it in the method and why we add self
print(Employee.fullname(emp_1)) # can also run these methods using the class name itself (Employee) but have to manually pass in instance as an argument