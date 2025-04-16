# # 1
# class Clock:
#     __DAY = 86400
    
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError('seconds must be an integer')
#         self.seconds = seconds % self.__DAY
        
#     def get_time(self) -> str:
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'
    
#     def __get_formatted(self, x):
#         return str(x).rjust(2, "0")
    
#     def __add__(self, other):
#         if not isinstance(other, (int, Clock)):
#             raise ArithmeticError('other must be an integer or Clock')
#         sc = other
#         if isinstance(other, Clock):
#             sc = other.seconds
        
#         return Clock(self.seconds + sc)
    
# c1 = Clock(86400)
# c2 = Clock(100)
# c3 = c1 + c2
# print(c1.get_time())


# # 2
# class Clock:
#     __DAY = 86400
    
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError('seconds must be an integer')
#         self.seconds = seconds % self.__DAY
        
#     def __eq__(self, value):
#         return self.seconds == value.seconds
    
# c1 = Clock(100)
# c2 = Clock(100)

# print(c1 == c2)


# 3
class Clock:
    __DAY = 86400
    
    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('seconds must be an integer')
        self.seconds = seconds % self.__DAY
        
    def __eq__(self, value):
        return self.seconds == value.seconds
    
    def __lt__(self, value):
        return self.seconds < value.seconds

    def __gt__(self, value):
        return self.seconds > value.seconds
    
    def __le__(self, value):
        return self.seconds <= value.seconds

    def __ge__(self, value):
        return self.seconds >= value.seconds

    
c1 = Clock(100)
c2 = Clock(100)

print(c1 == c2)

