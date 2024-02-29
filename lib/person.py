#!/usr/bin/env python3

class Person:
    # Class body goes here
    def talk(self):
        print("Hello World!")
    #Instance method definition
    def walk(self):
        print("The person is walking.")
    pass
fido = Person()
#To call talk and walk
fido.talk()
fido.walk()