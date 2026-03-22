n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)
pares = []
for valor in tupla:
    if valor % 2 == 0:
        pares.append(valor)
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    for i, valor in enumerate(tupla):
        if  valor == 3:       
            print(f'O valor 3 apareceu na {i+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
if pares:
    print(f'Os valores pares digitados foram {" ".join(map(str, pares))}') 
else:
    print('Nenhum valor par foi digitado')

