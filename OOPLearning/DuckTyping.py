'''
# Duck Typing and Asking Forgiveness, Not Permission (EAFP)
# Konsep : Walks as a Duck, Quacks as a Duck, and it's a Duck
# dont care what what type of object we are working with.
# we only care if are object can do what we asked to do.
'''
# Duck Typing and Easier to ask forgiveness than permission (EAFP)

# class Duck:
#
#     def quack(self):
#         print('Quack, quack')
#     def fly(self):
#         print('Flap, flap!')
#
# class Person:
#
#     def quack(self):
#         print('Iam quacking like a duck!')
#     def fly(self):
#         print('iam flapping my arms!')
#
# def quack_and_fly(thing):
#
#     # # not Duck-typed(non-Pythonic)
#     # if isinstance(thing, Duck):
#     #     thing.quack()
#     #     thing.fly()
#     # else:
#     #     print('This has to be a duck!')
#
#     # # LBYL (Non-Pythonic)
#     # if hasattr(thing, 'quack'):
#     #     if callable(thing.quack):
#     #         thing.quack()
#     # if hasattr(thing, 'fly'):
#     #     if callable(thing.fly):
#     #         thing.fly()
#
#     # EAFP(pythonic)
#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()
#     except AttributeError as e:
#         print(e)
#
#     print()
#
# d = Duck()
# quack_and_fly(d)
#
# p = Person()
# quack_and_fly(p)

# # person = {'name':'Jones', 'age': 23, 'job': 'Programmer'}
# person = {'name':'Jones', 'age':23}
#
# # # LBYL(non-Pythonic)
# # if 'name' in person and 'age' in person and 'job' in person:
# #     print('Iam {name}. iam {age} years old and iam a {job}'.format(**person))
# # else:
# #     print('Missing some keys')
#
# # EAFP(pythonic)
# try:
#     print('iam {name}. iam {age} years old and iam a {job}'.format(**person))
# except KeyError as e:
#     print('Missing {} key'.format(e))



# my_list = [1, 2, 3, 4, 5]
#
# # non-Pythonic
# if len(my_list) >= 6:
#     print(my_list[5])
# else:
#     print('that index does not exist')
#
# # pythonic(EAFP)
# try:
#     print(my_list[5])
# except IndexError:
#     print('that index doesnot exist')



import os

my_file = "/tmp/test.txt"

# race condition
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('File cannot be accessed')

# No-Race Condition
try:
    f = open(my_file)
except IOError as e:
    print('File Cannot be accessed')
else:
    with f:
        print(f.read())