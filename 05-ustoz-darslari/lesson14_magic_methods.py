# # 1
# class Points:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __call__(self, *args, **kwds):
#         return self.x, self.y
    
# pt = Points(1,2)
# print(pt())


# 2
class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @staticmethod
    def area(r):
        return 3.14 * r * r

pt = Points(1,2)
print(pt.area(3))
