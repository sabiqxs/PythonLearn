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

    # special method, method yg sudah ada di librari tetapi di definisikan kembali menjadi suatu fungsi yang di inginkan
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    def __add__(self, other):
        return  self.pay + other.pay
    def __len__(self):
        return len(self.fullname()) - 1
dev_1 = Employee('Nana', 'Ninas', 70000)
dev_2 = Employee('Test', 'User', 50000)

print(dev_1.fullname())

print(len(dev_1))