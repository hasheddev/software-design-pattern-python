class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    index = 0
    def create_person(self, name):
        person =  Person(self.index, name)
        self.index += 1
        return person