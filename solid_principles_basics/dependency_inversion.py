#High level modules should depend on abstractions and not on low level classes i.e depend on interfaces
from abc import ABC, abstractmethod
from enum import Enum
from typing import Generator

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name


class RelationshipsV:
    def __init__(self):
        self.relations: list[tuple[Person, Relationship, Person]] = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

class ResearchV:
    def __init__(self, relationships: RelationshipsV):
        relations = relationships.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John has a child called {r[2].name}")

parent = Person("John")
child1 = Person('Chris')
child2 = Person("Matt")

relationships = RelationshipsV()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

ResearchV(relationships)
#Research accesses low level relationship internal state which might break

class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children(self, name) -> Generator[str, None, None]:
        pass

class Relationships(RelationshipBrowser):
    def __init__(self):#low level might use db or other storage
        self.relations: list[tuple[Person, Relationship, Person]] = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children(self, name: str):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
               yield r[2].name
        

class Research:#high level module
    def __init__(self, browser: RelationshipBrowser, name: str):
        for cn in browser.find_all_children(name):
            print(f"{name} has a child {cn}")


relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
Research(relationships, "John")