# Single Responsibility
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override, Union

@dataclass
class Data:
    name:str
    description: str
    
    def save(self):
        print(f'Save {self.name}, {self.description}')
    
    def parse(self):
        print(f"Parse {self.name}, {self.description}")

class Save:
    def __init__(self, data_: Data):
        self.__data = data_
    
    def save_to_db(self):
        print(f"Save {self.__data.name}, {self.__data.description}")

class Parse:
    def __init__(self):
        pass