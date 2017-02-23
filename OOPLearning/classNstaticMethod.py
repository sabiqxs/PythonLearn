'''
regular Method = in a class automatically takes the instance as the first argument(self)
classMethod menggunakan simbol @classmethod. in class automatically receive the class for the first argument(cls) in the instance
staticMethod is not pass anything for the first argument
'''

class Employee:
    num_of_employee = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@Company.com'

        Employee.num_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls (first, last, pay)

    @staticmethod
    def is_workday(day):
        #saturday 5, sunday 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 70000)
emp_2 = Employee('Test', 'User', 50000)

Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Ali-Baba-50000'
emp_str_3 = 'Boys-Sueb-80000'

# first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2017, 2, 18)
print(Employee.is_workday(my_date))