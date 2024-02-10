taomlar = ['somsa','manti','honim','kabob','osh']
nonushta = taomlar[:]
nonushta.remove('honim')
del nonushta[1]
nonushta.remove('kabob')
nonushta.append('kasha')
nonushta.insert(0,'sir')
print(nonushta)

nonushta = tuple(nonushta)
nonushta = list(nonushta)
nonushta[0] = 'qaymoq va non'
print(nonushta)