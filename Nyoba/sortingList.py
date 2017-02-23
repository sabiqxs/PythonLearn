list = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_list = sorted(list, reverse=True)
print('Sorted Variable:\t', s_list)
list.sort(reverse=True)
print('original variable:\t', list)

tup = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_tup = sorted(tup, reverse=True)
print('Tuple\t', s_tup)
# tup.sort()
print('original Tuple:\t', tup)

di = {'name': 'Corey', 'job':'Programming', 'age':None, 'os':'Mac'}
s_dict = sorted(di, reverse=True)
print('Dict:\t', s_dict)
print('original dict:\t', di)


lis = [-6, -5, -4, 1, 2, 3]
s_lis = sorted(lis, key=abs)
print(s_lis)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('Putri', 20, 50000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.salary

# s_employees = sorted(employees, key=e_sort, reverse=True)
# s_employees = sorted(employees, key=lambda e:e.name)

from operator import attrgetter
s_employees = sorted(employees, key=attrgetter('age'))


print(s_employees)