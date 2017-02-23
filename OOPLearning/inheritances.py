class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@Company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        # super(Developer, self).__init__(first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        # super(Manager, self).__init__(first, last, pay)
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Nana', 'Nina', 70000, 'python')
dev_2 = Developer('Test', 'User', 50000, 'java')

mgr_1 = Manager('Sue', 'Janu', 90000, [dev_1])

# print(isinstance(dev_1, Developer))
# print(issubclass(Manager, Developer))
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emp()

# dev_1.apply_raise()
# print(dev_1.prog_lang)
