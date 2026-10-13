class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObervable:
    def __init__(self) -> None:
        self.property_changed = Event()


class Person(PropertyObervable):
    def __init__(self, age=0) -> None:
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed("Person:age", value)


class TrafficAuthority:
    def __init__(self, person:Person) -> None:
        self.person = person
        self.person.property_changed.append(self.person_changed)

    def person_changed(self, property_name, value):
        if property_name == "Person:age":
            if value < 16:
                print("Sorry, you still cannot drive")
            else:
                print("Okay, you can drive")
                self.person.property_changed.remove(self.person_changed)


if __name__ == "__main__":
    person = Person()
    ta = TrafficAuthority(person)
    for age in range (14, 20):
        print(f"setting age to {age}")
        person.age = age
