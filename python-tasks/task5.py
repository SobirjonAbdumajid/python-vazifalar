Sonlar  = [3,11,33,99,-11,99.9]
print(Sonlar)

Sonlar[-1] = Sonlar[-1] - 0.9
print(Sonlar)

del Sonlar[-1]
print(Sonlar)

Sonlar.insert(-1,0)
print(Sonlar)

Sonlar.remove(0)
print(Sonlar)

Sonlar.append(0)
print(Sonlar)