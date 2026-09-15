class Person:
    def __init__(self):
        self.name= None
        self.date_of_birth = None
        self.position = None

    def __str__(self) -> str:
        return f"""Name: {self.name}, DOB {self.date_of_birth}, Job {self.position}"""

    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def work_as(self, position):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, dob):
        self.person.date_of_birth = dob
        return self
