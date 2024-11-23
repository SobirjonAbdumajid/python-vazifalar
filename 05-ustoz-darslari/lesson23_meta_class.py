# # 1
# A = type('Point', (), {'x':0, 'y':0})

# a = A()
# # a.x = 3
# print(a.x)


# 2
class Women:
    women_id = "This is women id"
    women_name = "This is women name"
    women_age = "This is women age"

    def __init__(self, login, pasw):
        self.login = login
        self.pasw = pasw
        self.meta = self.Meta(login + "@" + pasw)
    
    class Meta:
        def __init__(self, access):
            self._access = access

w = Women('root', '1234')
print(w.__dict__)
print(w.meta.__dict__)
        