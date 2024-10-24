student = [
    ('Alina', [1, 3, 2]),
    ('Ivan', [4, 1, 4]),
    ('Charlie', [7, 3, 5]),
    ('Islam', [4, 2, 2]),
]

result = 0
_dict = {}

for i in student:
    for j in i[1]:
        result += j
    _dict[f"{i[0]}"] = result
    result = 0

sorted_students = sorted(_dict.items(), key=lambda item: item[1], reverse=True)

for student, score in sorted_students:
    print(f"{student}: {score}")
