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

    @abstractmethod
    def additional_operation(self) -> str:
        pass

    @abstractmethod
    def status_check(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."

    def additional_operation(self) -> str:
        return "ConcreteImplementationA: Performing additional operation."

    def status_check(self) -> str:
        return "ConcreteImplementationA: Status is OK."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."

    def additional_operation(self) -> str:
        return "ConcreteImplementationB: Performing additional operation."

    def status_check(self) -> str:
        return "ConcreteImplementationB: Status is OK."


class ConcreteImplementationC(Implementation):  # Yangi qurilma
    def operation_implementation(self) -> str:
        return "ConcreteImplementationC: Here's the result on the Smart Speaker."

    def additional_operation(self) -> str:
        return "ConcreteImplementationC: Performing additional operation."

    def status_check(self) -> str:
        return "ConcreteImplementationC: Status is OK."


class UniversalRemoteControl(Abstraction):  # Universal pult
    def __init__(self, devices: list[Implementation]) -> None:
        self.devices = devices

    def operation(self) -> str:
        results = "\n".join(device.operation_implementation() for device in self.devices)
        return f"UniversalRemoteControl: Controlling multiple devices:\n{results}"

    def perform_additional_operations(self) -> str:
        results = "\n".join(device.additional_operation() for device in self.devices)
        return f"UniversalRemoteControl: Performing additional operations:\n{results}"

    def check_statuses(self) -> str:
        results = "\n".join(device.status_check() for device in self.devices)
        return f"UniversalRemoteControl: Checking statuses:\n{results}"


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
    print("\n")
    print(universal_remote.perform_additional_operations())
    print("\n")
    print(universal_remote.check_statuses())
