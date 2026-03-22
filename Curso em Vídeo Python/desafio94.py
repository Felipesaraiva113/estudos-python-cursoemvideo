dados = {}
grupo = []
ages = []
mulheres = []
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    ages.append(dados['idade'])
    grupo.append(dados.copy())
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
    if sn == 'N':
        break   
print('-='*40)
print(f'- O grupo tem {len(grupo)} pessoas.')
mi = sum(ages)/len(ages)
print(f'- A média de idade é de {mi:.2f} anos.')
print('- As mulheres cadastradas foram:',end=' ')
for i in mulheres:
    print(i, end = ' ')
print()
print('- Lista das pessoas que estão acima da média:')
for e in grupo:
    for k, v in e.items():
        if k == 'idade':
            if v > mi:
                print()
                for k, v in e.items():
                    print(f'{k} = {v};', end=' ')
                print()
print('<< ENCERRADO >>')
