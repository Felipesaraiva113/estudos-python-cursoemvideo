qtd = int(input('digite quantos termos sa sequência de fibonacci devo mostrar: '))
i = 0
n1 = 0
n2 = 1
s = 0
n3 = 0
if qtd > 1:
    print(n1)
    print(n2)
    while i < qtd - 2:
        i += 1
        s = n1 + n2
        n3 = s
        n1 = n2
        n2 = n3
        print(n3)
elif qtd == 1:
    print(n1)