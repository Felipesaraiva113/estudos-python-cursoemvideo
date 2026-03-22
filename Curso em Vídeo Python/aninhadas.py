nome = str(input('qual é seu nome? '))
if nome == 'Gustavo':
    print('que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('seu nome é bem comum no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('que belo nome feminino!')
else:
    print('seu nome é bem normal.')
print(f'tenha um bom dia, {nome}!')