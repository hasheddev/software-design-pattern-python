from abc import ABC, abstractmethod

# ==========================================
# 1. THE IMPLEMENTATION INTERFACE
# ==========================================
class Device(ABC):
    """
    The Implementation defines the interface for all low-level devices.
    """
    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass


# ==========================================
# 2. CONCRETE IMPLEMENTATIONS
# ==========================================
class TV(Device):
    def __init__(self):
        self._on = False

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        print("TV: Turning ON")
        self._on = True

    def disable(self) -> None:
        print("TV: Turning OFF")
        self._on = False


class Radio(Device):
    def __init__(self):
        self._on = False

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        print("Radio: Powering up transmitters")
        self._on = True

    def disable(self) -> None:
        print("Radio: Going silent")
        self._on = False


# ==========================================
# 3. THE ABSTRACTION
# ==========================================
class RemoteControl:
    """
    The Abstraction maintains a reference (bridge) to a Device object.
    It delegates the actual work to that object.
    """
    def __init__(self, device: Device):
        self.device = device  # This reference is the "Bridge"

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()


# ==========================================
# 4. REFINED ABSTRACTION
# ==========================================
class AdvancedRemoteControl(RemoteControl):
    """
    You can extend the Abstraction independently without changing the Devices.
    """
    def mute(self) -> None:
        print("Advanced Remote: Muting the device!")
        self.device.disable()


# ==========================================
# 5. CLIENT CODE
# ==========================================
if __name__ == "__main__":
    # Create the concrete implementations
    tv = TV()
    radio = Radio()

    print("--- Using Basic Remote with TV ---")
    basic_remote = RemoteControl(tv)
    basic_remote.toggle_power()
    basic_remote.toggle_power()

    print("\n--- Using Advanced Remote with Radio ---")
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power()
    advanced_remote.mute()
