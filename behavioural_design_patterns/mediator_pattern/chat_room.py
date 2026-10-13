class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session {s}]")
        self.chat_log.append(s)

    def private_message(self, who, message):
        if self.room:
            self.room.message(self.name, who, message)

    def say(self, message):
        if self.room:
            self.room.broadcast(self.name, message)

    def exit_room(self):
        if self.room:
            self.room.leave(self)


class ChatRoom:
    def __init__(self) -> None:
        self.people = []

    def join(self, person):
        join_msg = f"{person.name} joins chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def leave(self, person):
        if person in self.people:
            self.people.remove(person)
            exit_msg = f"{person.name} left chat"
            person.room = None
            self.broadcast("room", exit_msg)

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == "__main__":
    john = Person("john")
    jane = Person("jane")
    monk = Person("monk")
    chat = ChatRoom()
    chat.join(john)
    chat.join(jane)
    chat.join(monk)
    john.say("Hi every body")
    jane.say("Hey john")
    john.exit_room()
    jane.private_message(monk.name, "Hello monk")