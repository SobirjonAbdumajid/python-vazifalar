from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


class ConcreteImplementationC(Implementation):  # Yangi qurilma
    def operation_implementation(self) -> str:
        return "ConcreteImplementationC: Here's the result on the Smart Speaker."


class UniversalRemoteControl(Abstraction):  # Universal pult
    def __init__(self, devices: list[Implementation]) -> None:
        self.devices = devices

    def operation(self) -> str:
        results = "\n".join(device.operation_implementation() for device in self.devices)
        return f"UniversalRemoteControl: Controlling multiple devices:\n{results}"


# Test qilish
if __name__ == "__main__":
    implementationA = ConcreteImplementationA()
    implementationB = ConcreteImplementationB()
    implementationC = ConcreteImplementationC()

    abstraction = Abstraction(implementationA)
    print(abstraction.operation())

    print("\n")

    abstraction = ExtendedAbstraction(implementationB)
    print(abstraction.operation())

    print("\n")

    universal_remote = UniversalRemoteControl([implementationA, implementationB, implementationC])
    print(universal_remote.operation())
