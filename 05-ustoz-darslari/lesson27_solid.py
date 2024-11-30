# Single Responsibility
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override, Union


@dataclass
class Data:
    name: str
    description: str

    def save(self):
        print(f"Save {self.name}, {self.description}")

    def parse(self):
        print(f"Parse {self.name}, {self.description}")


class Save:
    def __init__(self, data_: Data):
        self.__data = data_

    def save_to_db(self):
        print(f"Save {self.__data.name}, {self.__data.description}")


class Parse:
    def __init__(self, data_: Data):
        self.__data = data_

    def parse_to_db(self):
        print(f"Parse {self.__data.name}, {self.__data.description}")


# Open-closed
class Figure:
    def draw(self):
        print("This is draw figure")


class Line(Figure):
    @override
    def draw(self):
        print("This is Line class")


class Circle(Figure):
    @override
    def draw(self):
        print("This is Circle class")


class Polygon(Figure):
    @override
    def draw(self):
        print("This is Polygon class")


class Square(Figure):
    @override
    def draw(self):
        print("This is Square class")

    def info(self):
        print("This is info function")


# Liskov Substitution
class DrawProcess:
    def __init__(self, figure: Figure):
        self.__figure = figure

    def draw_figure(self):
        self.__figure.draw()


# Interface Segregation
class Developer(ABC):
    @abstractmethod
    def write_code(self):
        pass


class Tester(ABC):
    @abstractmethod
    def testing_code(self):
        pass


class BackendDeveloper(Developer, Tester):
    @override
    def write_code(self):
        print("BackendDeveloper write code")

    @override
    def testing_code(self):
        print("BackendDeveloper test code")


class FrontendDeveloper(Developer, Tester):
    @override
    def write_code(self):
        print("FrontendDeveloper write code")

    @override
    def testing_code(self):
        print("FrontendDeveloper test code")


class TesterEngineer(Tester):
    @override
    def testing_code(self):
        print("Tester test code")


class FlutterDeveloper(Developer, Tester):
    @override
    def write_code(self):
        print("FlutterDeveloper write code")

    @override
    def testing_code(self):
        print("FlutterDeveloper test code")


# DEPENDENCY INVERSION
class WorkingEngineer:
    def __init__(self, engineer: Union[Tester, Developer]):
        self.__engineer = engineer

    def working_code(self):
        if isinstance(self.__engineer, Tester) and not isinstance(self.__engineer, Developer):
            self.__engineer.testing_code()
        elif isinstance(self.__engineer, Union[Developer, Tester]):
            self.__engineer.write_code()
            self.__engineer.testing_code()


def main():
    we = WorkingEngineer(FlutterDeveloper())
    we.working_code()


if __name__ == "__main__":
    main()
