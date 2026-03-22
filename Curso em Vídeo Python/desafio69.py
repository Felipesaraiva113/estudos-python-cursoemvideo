def linhas():
    print('-' * 28)
maior = []
homens = 0
mulheres = 0
while True:
    linhas()
    print('    CADASTRE UMA PESSOA')
    linhas()
    i = int(input('Idade: '))
    if i > 18:
        maior.append(i)
    while True: 
        s = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if s in 'MF':
            break
    if s == 'M':
        homens += 1
    if s == 'F':
        if i < 20:
            mulheres += 1
    linhas()
    while True:
        sn = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
        if sn in 'SN':
            break
    if sn == 'N':
        print('====== FIM DO PROGRAMA ======')
        break
maior_qtd = len(maior)
print(f'Total de pessoas com mais de 18 anos: {maior_qtd}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
