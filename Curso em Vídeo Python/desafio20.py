from random import shuffle
a1 = input('aluno 1: ')
a2 = input('aluno 2: ')
a3= input('aluno 3: ')
a4 = input('aluno 4: ')
l = [a1, a2 , a3, a4]
e = shuffle(l)
print(f'ordem de apresentação dos trabalhos: {l}')