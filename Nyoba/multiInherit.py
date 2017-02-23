class Mario():
    def move(self):
        print("iam moved out")

class Jamur():
    def eat_jamur(self):
        print("now iam bigger")

# inheritence untuk 2 class
class BigMarioTeguh(Mario, Jamur):
    pass

besar = BigMarioTeguh()
besar.eat_jamur()
besar.move()