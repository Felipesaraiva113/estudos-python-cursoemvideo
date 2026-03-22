from random import randint
dicionario = {}
pos = 1
print('Valores sorteados: ')
for i in range(1,5):
    l = randint(1,6)    
    dicionario[f'jogador{i}'] = l
    print(f'   O jogador{i} tirou {l}')
diciord = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse= True))
print('Ranking dos jogadores:')
for j,v in diciord.items():
    print(f'   {pos}° lugar: {j} com {v}')
    pos += 1
