import copy


class Address:
    def __init__(self, street_address, city, country) -> None:
        self.city = city
        self.street_address = street_address
        self.country = country
    
    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}, {self.country}"

class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} lives at {self.address}"


john = Person("John", Address("123 London road", "London", "UK"))
print(john)
# jane = john
# jane.name = "Jane"
# print(jane)
# print(john)

jane = copy.deepcopy(john)
jane.name = "Jane"
jane.address.street_address = "184 london road"
print(jane)
print(john)