grupo = []
dados = []
tot = 0
num = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    grupo.append(dados[:])
    tot += 1
    dados.clear()
    sn = str(input('Quer continuar? [S/N] ')).strip().upper()
    if sn == 'N':
        break
for p in grupo:
    num.append(p[1])
mp = max(num)
mep = min(num)
print('-='*30)
print(f'Ao todo, você cadastrou {tot} pessoas')
print(f'O maior peso foi de {mp}Kg. Peso de ', end = '')
for i in range(len(grupo)):
    if grupo[i][1] == mp:
        print(grupo[i][0], end = ' ')
print(f'\nO menor peso foi de {mep}Kg. Peso de ', end = '')  
for i in range(len(grupo)):
    if grupo[i][1] == mep:
        print(grupo[i][0], end = ' ')
