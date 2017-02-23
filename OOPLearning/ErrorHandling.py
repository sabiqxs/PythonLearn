

try:
    f = open('corupt_file.txt')
    # if f.name == 'corupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
    print('Error')
else:
    print(f.read())
    f.close()
finally:
    print('executing finally')
