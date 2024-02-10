friends = []
friends.append('Sardorbek')
friends.append('Umidjon')
friends.append('Abduqahhor')
friends.append('Ilhomjon')
friends.append('Abbos')
friends.append('Doniyor')
print(friends)

friends.remove('Doniyor')
print(friends)

friends.append('Sanjar')
friends.insert(0,"Jo'rabek")
friends.insert(3,"Muhsinjon")
print(friends)

mehmonlar = []

mehmonlar.append(friends[1])
mehmonlar.append(friends[2])
mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(4))
print(f'Kelgan mehmonlar: {mehmonlar}')