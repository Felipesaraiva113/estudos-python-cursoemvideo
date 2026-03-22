lista =[]
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    sn = str(input('Quer continuar? [S/N] ')).strip().upper()
    if sn == 'N':
        break
print('-='*30)  
lista.sort(reverse=True) 
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decresente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
