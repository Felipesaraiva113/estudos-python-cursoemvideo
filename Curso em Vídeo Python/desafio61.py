a1 = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razão: '))
c = a1
i = 1
total = 0
mais = 10
print(a1)
while mais != 0:
    total += mais
    while i < total:
        c += r
        i += 1
        print(c)
    mais = int(input(('quantos termos você quer mostrar a mais? ')))
print('fim.')



    

    




