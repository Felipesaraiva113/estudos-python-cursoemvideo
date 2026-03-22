from datetime import date
dicionario = {}
dicionario['nome'] = str(input('Nome: '))
an = int(input('Ano de nascimento: '))
dty = date.today().year
dicionario['idade'] = dty - an
clt = int(input('Carteira de trabalho (0 não tem): '))
dicionario['ctps'] = clt
if clt > 0:   
    dicionario['contratação'] = int(input('Ano de contratação: '))
    dicionario['salário'] = float(input('Salário: '))
    dicionario['aposentadoria'] = ((dicionario['contratação'] + 35)-dty) + dicionario['idade']
print('-='*50)
for k, v in dicionario.items():
    print(f'{k} tem o valor {v}')
