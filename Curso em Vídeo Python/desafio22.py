n = str(input('digite seu nome completo: '))
ma = n.upper()
mi = n.lower()
pn = n.split()
print(f'seu nome com todas as letras maiúsculas: {ma}')
print(f'seu nome com todas as letras minúsculas: {mi}')
print(f'quantas letras tem ao todo: {len(n.replace(" ", ""))}')
print(f'quantidade de letras do primeiro nome: {len(pn[0])}')

