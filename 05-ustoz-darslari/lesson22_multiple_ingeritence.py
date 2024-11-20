class Point:
    @staticmethod
    def draw():
        print("draw works")

class Logger:
    @staticmethod
    def save_log():
        print("Logger works")

class InsertDatabase:
    @staticmethod
    def insert():
        print("insert works")

class Notebook(Point, Logger, InsertDatabase):
    pass

n = Notebook()
n.draw()
n.save_log()
n.insert()
