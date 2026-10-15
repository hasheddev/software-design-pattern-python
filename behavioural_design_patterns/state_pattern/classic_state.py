from abc import ABC

class Switch:
    def __init__(self) -> None:
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):
    def on(self, switch):
        print(f"Light is already on")

    def off(self, switch):
        print(f"Light is already off")

class OffState(State):

    def __init__(self) -> None:
        print('Light is turned off')

    def on(self, switch):
        print(f"Turning light on...")
        switch.state = OnState()

class OnState(ABC):
    def __init__(self) -> None:
        print('Light is turned on')
    
    def off(self, switch):
        print(f"Turning light off...")
        switch.state = OffState()


if __name__ == "__main__":
    switch = Switch()
    switch.on()
    switch.off()
    switch.off()