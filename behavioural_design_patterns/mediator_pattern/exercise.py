from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)

class Mediator:
    def __init__(self) -> None:
        self.events = Event()

    def fire_event(self, sender, value):
        self.events(sender, value)

class Participant:
    def __init__(self, mediator: Mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.events.append(self.broadcast)

    def say(self, value):
        self.mediator.fire_event(self, value)

    def broadcast(self, sender, value):
        if sender != self:
            self.value += value