def tambah(num1, num2):
    return num1 + num2

def kurang(num1, num2):
    return num1 - num2

def bagi(num1, num2):
    return num1 / num2

def kali(num1, num2):
    return num1 * num2

def main():
    operation = input("pilih operand(+, -, /, *)\n")
    if (operation != "+" and operation != "-" and operation != "/" and operation != "*"):
        print("input tidak valid")
    else:
        var1 = int(input("angka pertama: "))
        var2 = int(input('angka kedua: '))
        if (operation == '+'):
            print(tambah(var1, var2))
        elif(operation == '-'):
            print(kurang(var1, var2))
        elif(operation == '/'):
            print(bagi(var1, var2))
        else:
            print(kali(var1, var2))

    respond = input("again: y/n\n")
    if (respond == 'y'):
        main()
    else:
        exit()
main()