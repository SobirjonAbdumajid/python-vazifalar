# # 1
# class Points:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __call__(self, *args, **kwds):
#         return self.x, self.y
    
# pt = Points(1,2)
# print(pt())


# # 2
# class Points:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     @staticmethod
#     def area(r):
#         return 3.14 * r * r

# pt = Points(1,2)
# print(pt.area(3))


# # 3
# class Student:
#     counter = 0
#     def __init__(self, name):
#         Student.counter += 1
#         self.name = name
#         print(self.name, self.counter)
        
#     @classmethod
#     def show_count_student(cls):
#         print(cls.counter)

# st1 = Student("Sobirjon")
# st2 = Student("Sardorbek")

# Student.show_count_student()



# class Counter:
#     counter = 0
#     def __init__(self, n):
#         self.n = n
#         Counter.counter += 1
    
#     @classmethod
#     def show_count(cls):
#         print(cls.counter)
        
#     def __call__(self, num):
#         result = 0
#         result += num
#         print(result)

# ct1 = Counter(2)    
# ct2 = Counter(3)    
# ct3 = Counter(4)
# ct1()
# Counter.show_count()


# class Counter:
#     counter = 0

#     def __init__(self, n):
#         self.n = n
#         Counter.counter += 1

#     @classmethod
#     def show_count(cls):
#         print("Counter:", cls.counter)
        
#     def __call__(self, num=0):
#         result = self.n
#         result += num
#         print(result)

# ct1 = Counter(2)    
# ct2 = Counter(3)    
# ct3 = Counter(4)

# ct3()
# Counter.show_count()


# class Counter:
#     counter = 0
#     counter2 = 0

#     def __call__(self, *args, **kwargs):
#         return Counter.counter
    
    

# ct1 = Counter()
# print(ct1(3))
# print(ct1(2))

# print(Counter.counter2)


# class Counter:
#     counter = 0
#     counter2 = 0

#     def __call__(self, num):
#         Counter.counter += num
#         Counter.counter2 += 1
#         return Counter.counter

# ct1 = Counter()
# print(ct1(3))  # Increments by 3
# print(ct1(2))  # Increments by 2, total should be 5
# print(Counter.counter2)  # Counts the number of calls

class Counter:
    def __init__(self):
        self.total = 0
        self.count = 0
    
    def __call__(self, X):
        self.total += X
        self.count += 1
        print(self.total)

    def show_count(self):
        print(self.count)
    
ct = Counter()
ct(1)
ct(3)
ct(6)
ct(1)
ct.show_count()
