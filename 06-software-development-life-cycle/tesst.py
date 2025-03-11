# from __future__ import annotations
# from abc import ABC, abstractmethod
#
#
# class Abstraction:
#     """
#     The Abstraction defines the interface for the "control" part of the two
#     class hierarchies. It maintains a reference to an object of the
#     Implementation hierarchy and delegates all of the real work to this object.
#     """
#
#     def __init__(self, implementation: Implementation) -> None:
#         self.implementation = implementation
#
#     def operation(self) -> str:
#         return (f"Abstract+ion: Base operation with:\n"
#                 f"{self.implementation.operation_implementation()}")
#
#
# class ExtendedAbstraction(Abstraction):
#     """
#     You can extend the Abstraction without changing the Implementation classes.
#     """
#
#     def operation(self) -> str:
#         return (f"ExtendedAbstraction: Extended operation with:\n"
#                 f"{self.implementation.operation_implementation()}")
#
#
# class Implementation(ABC):
#     """
#     The Implementation defines the interface for all implementation classes. It
#     doesn't have to match the Abstraction's interface. In fact, the two
#     interfaces can be entirely different. Typically the Implementation interface
#     provides only primitive operations, while the Abstraction defines higher-
#     level operations based on those primitives.
#     """
#
#     @abstractmethod
#     def operation_implementation(self) -> str:
#         pass
#
#
# """
# Each Concrete Implementation corresponds to a specific platform and implements
# the Implementation interface using that platform's API.
# """
#
#
# class ConcreteImplementationA(Implementation):
#     def operation_implementation(self) -> str:
#         return "ConcreteImplementationA: Here's the result on the platform A."
#
#
# class ConcreteImplementationB(Implementation):
#     def operation_implementation(self) -> str:
#         return "ConcreteImplementationB: Here's the result on the platform B."
#
#
# def client_code(abstraction: Abstraction) -> None:
#     """
#     Except for the initialization phase, where an Abstraction object gets linked
#     with a specific Implementation object, the client code should only depend on
#     the Abstraction class. This way the client code can support any abstraction-
#     implementation combination.
#     """
#
#     # ...
#
#     print(abstraction.operation(), end="")
#
#     # ...
#
#
# if __name__ == "__main__":
#     """
#     The client code should be able to work with any pre-configured abstraction-
#     implementation combination.
#     """
#
#     implementation = ConcreteImplementationA()
#     abstraction = Abstraction(implementation)
#     client_code(abstraction)
#
#     print("\n")
#
#     implementation = ConcreteImplementationB()
#     abstraction = ExtendedAbstraction(implementation)
#     client_code(abstraction)
#
#
#
# class ConcreteImplementationC(Implementation):
#     def operation_implementation(self) -> str:
#         return "ConcreteImplementationC: Yugurdim suvli yo'lda, splash-splash!"
#
# implementation = ConcreteImplementationC()
# abstraction = Abstraction(implementation)
# client_code(abstraction)


from __future__ import annotations
from abc import ABC, abstractmethod


class RemoteController:
    def __init__(self, device: Device) -> None:
        self.device = device

    def toggle_power(self) -> str:
        return f"RemoteController: Toggling power...\n{self.device.power_switch()}"

    def adjust_volume(self, level: int) -> str:
        return f"RemoteController: Adjusting volume to {level}...\n{self.device.set_volume(level)}"

    def change_channel(self, channel: int) -> str:
        return f"RemoteController: Changing channel to {channel}...\n{self.device.change_channel(channel)}"


class AdvancedRemoteController(RemoteController):
    def mute(self) -> str:
        return f"AdvancedRemoteController: Muting...\n{self.device.set_volume(0)}"

    def toggle_power(self) -> str:
        return f"AdvancedRemoteController: Toggling power with advanced features...\n{self.device.power_switch()}"


class Device(ABC):
    @abstractmethod
    def power_switch(self) -> str:
        pass

    @abstractmethod
    def set_volume(self, level: int) -> str:
        pass

    @abstractmethod
    def change_channel(self, channel: int) -> str:
        pass


class TV(Device):
    def power_switch(self) -> str:
        return "TV: Power toggled ON/OFF."

    def set_volume(self, level: int) -> str:
        return f"TV: Volume set to {level}."

    def change_channel(self, channel: int) -> str:
        return f"TV: Channel changed to {channel}."


class DVDPlayer(Device):
    def power_switch(self) -> str:
        return "DVDPlayer: Power toggled ON/OFF."

    def set_volume(self, level: int) -> str:
        return f"DVDPlayer: Volume set to {level}."

    def change_channel(self, channel: int) -> str:
        return f"DVDPlayer: Channel changed to {channel}."


def client_code(remote: RemoteController) -> None:
    print(remote.toggle_power())
    print(remote.adjust_volume(50))
    print(remote.change_channel(5))
    if isinstance(remote, AdvancedRemoteController):
        print(remote.mute())


if __name__ == "__main__":
    tv = TV()
    basic_remote = RemoteController(tv)
    print("Using Basic Remote with TV:")
    client_code(basic_remote)

    print("\n")

    dvd = DVDPlayer()
    advanced_remote = AdvancedRemoteController(dvd)
    print("Using Advanced Remote with DVD Player:")
    client_code(advanced_remote)
