def linhas():
    print('-'*41)
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
linhas()
print('           LISTAGEM DE PREÇOS')
linhas()
for valor in range(0, len(listagem), 2):
    print(f'{listagem[valor]:.<30}', end= ' ')
    print(f'R$', end = '' )
    print(f'{listagem[valor+1]:>7.2f}')
linhas()    
