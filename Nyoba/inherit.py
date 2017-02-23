class Parent():

    def print_last_name(self):
        print("Safrudin")


# inherit untuk satu class
class Child(Parent):

    def print_first_name(self):
        print("Sabiq")
    def print_last_name(self):
        print("Al Hasby")
sabiq = Child()
sabiq.print_first_name()
sabiq.print_last_name()