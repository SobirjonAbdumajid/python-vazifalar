_list = [x for x in range(1,5)]
print(_list)

_set = {y for y in range(1,5)}
print(_set)

names = ["Alex", "Ivan", "Sergey"]
_dict = {x:y for x, y in enumerate(names)}
print(_dict)


_tuple = (y for y in range(1,5))
print(_tuple)
