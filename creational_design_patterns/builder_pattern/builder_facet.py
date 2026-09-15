#two separate builders for address and employment info
class Person:
    def __init__(self):
        #address
        self.street_address = None
        self.postcode = None
        self.city = None
        #employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f"""Address: {self.street_address}, {self.postcode}, {self.city}
            Employed at {self.company_name} as a {self.position} earning {self.annual_income}"""

#violates open closed principle as we have to modify to add new builder
class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def works_at(self, company_name):
        self.person.company_name = company_name
        return self

    def position(self, job_position):
        self.person.position = job_position
        return self

    def annual_income(self, income):
        self.person.annual_income = income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def lives_at(self, street_addr):
        self.person.street_address = street_addr
        return self

    def postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def city(self, city):
        self.person.city = city
        return self

pb = PersonBuilder()

person = pb.lives.\
            lives_at("143 london road")\
            .city("London")\
            .postcode('sw12b')\
            .works.annual_income(123000)\
            .position("Engineer")\
            .works_at("Fabrikam")\
            .build()

print(person)