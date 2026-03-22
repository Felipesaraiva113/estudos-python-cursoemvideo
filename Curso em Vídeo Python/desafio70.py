def linhas():
    print('-' * 28)
linhas()
print('       Beta Informática')
linhas()
s = 0
tot = 0
nome = []
preço = []
while True:
    np = str(input('Nome do produto: '))
    nome.append(np)
    pp = float(input('Preço: R$'))
    preço.append(pp)
    s += pp
    if pp > 1000:
        tot += 1
    while True:
        sn = str(input('Quer continuar [S/N]: ')).upper().strip()
        if sn.startswith('S') or sn.startswith('N'):
            break
    if sn == 'N':
        print('----------- FIM DO PROGRAMA -----------')
        break 
pmb = min(preço)
indice = preço.index(pmb)
nmb = nome[indice]
print(f'O total da compra foi R${s:.2f}')
print(f'Temos {tot} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nmb} que custa R${pmb:.2f}') 
