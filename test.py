#!/usr/bin/env python3


class var(object):
    def __init__(self, value):
        self.value = value

    def printx(self):
        print(str(self.value))

    def square(self):
        if type(self.value) == 'int':
            self.value = self.value ** 2
        return self.value


string = var("Hello World")

string.printx()

age = var(15)

age.printx()

age = age.square()

age.printx()
