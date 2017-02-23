class Employee:
    num_of_employee = 0
    raise_amount = 1.04
    #membuat Instance Variabel pada init method
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

print(Employee.num_of_employee)
emp_1 = Employee('Corey', 'Schafer', 70000)
emp_2 = Employee('Test', 'User', 50000)

''' No need to use this code, because we have init method as a constuctor.
emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.sc@mail.com'
emp_1.pay = 70000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'User.sc@mail.com'
emp_2.pay = 50000
'''

print (emp_1.email)
print(emp_1.fullname())

#or we can use this code = emp_1.fullname() dengan langsung menggunakan class Employee
print(Employee.fullname(emp_1))

print(emp_1.pay)
#menjalankan function apply_raise sehingga nilai akan naik
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)

#melihat keseluruhan
print(emp_1.__dict__)
print(emp_2.__dict__)

print(Employee.num_of_employee)