# # 1
# class Point:
#     @staticmethod
#     def draw():
#         print("draw works")

# class Logger:
#     @staticmethod
#     def save_log():
#         print("Logger works")

# class InsertDatabase:
#     @staticmethod
#     def insert():
#         print("insert works")

# class Notebook(Point, Logger, InsertDatabase):
#     pass

# n = Notebook()
# n.draw()
# n.save_log()
# n.insert()


# 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def draw():
        print("draw works")

class Logger:
    def __init__(self):
        super.__init__()
    @staticmethod
    def save_log():
        print("Logger works")


class Notebook(Point, Logger):
    pass

n = Notebook(1,2)
n.draw()
n.save_log()
