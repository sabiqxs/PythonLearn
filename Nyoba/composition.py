class Head(object):

    def __init__(self, eye_color, hair_color):
        self.eye_color = eye_color
        self.hair_color = hair_color

class Body(object):

    def __init__(self, weight):
        self.weight = weight

class Person(object):

    def __init__(self, eye_color, hair_color, weight):
        self.head = Head(eye_color, hair_color)
        self.body = Body(weight)

    def print_eye_color(self):
        print(self.head.eye_color)
        print(self.head.hair_color)
        print(self.body.weight)

sabiq = Person('blue', 'blonde', 160)
sabiq.print_eye_color()