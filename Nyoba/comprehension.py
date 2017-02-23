nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# mylist = []
# for n in nums:
#     mylist.append(n*n)
# print(mylist)

# mylist = [n*n for n in nums]
# print(mylist)

# mylist = map(lambda n: n*n, nums)
# print(mylist)

# mylist = []
# for n in nums:
#     if n%2 == 1:
#         mylist.append(n)
# print(mylist)

# mylist = [n for n in nums if n%2==0]
# print(mylist)

# mylist = filter(lambda n: n%2 == 0, nums)
# print(mylist)

# mylist= []
# for letter in 'abcd':
#     for num in range(4):
#         mylist.append((letter, num))
# print (mylist)

# mylist = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(mylist)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# myDict = {}
# for name, hero in zip(names, heroes):
#     myDict[name] = hero
# print(myDict)

# # menampilkan hero selain peter.
# myDict = {name : hero for name, hero in zip(names, heroes) if name != 'Peter'}
# print(myDict)

# set Comprehension
# numbs = [1, 1, 2, 1, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# mySet = {n for n in numbs}
# print(mySet)

# Generator Expression
# i want to Yield 'n*n' for each 'n' in nums

def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)
for i in my_gen:
    print(i)

#     atau bisa menggunakan syntax ini
# myGen = (n*n for n in nums)
# for i in myGen:
#     print(i)