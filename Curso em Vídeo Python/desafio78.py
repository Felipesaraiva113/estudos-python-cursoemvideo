lista = []
for i in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))
print('=-'*30)
print(f'Você digitou os valores {lista}')
mai = max(lista)
me = min(lista)
print(f'O maior valor digitado foi {mai} nas posições', end=' ')
for pos, v in enumerate(lista):
    if v==mai:
        print(f'{pos}...',end=' ')        
print(f'\nO menor valor digitado foi {me}nas posições', end=' ')
for pos, v in enumerate(lista):
    if v==me:
        print(f'{pos}...',end=' ') 
