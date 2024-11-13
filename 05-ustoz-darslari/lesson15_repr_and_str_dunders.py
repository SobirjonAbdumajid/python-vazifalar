class Cat:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'{self.__class__}: {self.name}'
    
    def __str__(self):
        return self.name
    
ct = Cat("Alex")
print(ct)
print(str(ct))
