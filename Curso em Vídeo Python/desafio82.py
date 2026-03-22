lista =[]
pares = []
imp = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 ==0:
        pares.append(n)
    else:
        imp.append(n)
    sn = str(input('Quer continuar? [S/N] ')).strip().upper()
    if sn == 'N':
        break
print('-='*30)  
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {imp}')
