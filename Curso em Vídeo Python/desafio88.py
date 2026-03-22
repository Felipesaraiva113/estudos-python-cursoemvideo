from random import sample
from time import sleep
lista = []
jogos = []
def linhas():
    print('-'*38)
linhas()
print('         JOGUE NA MEGA SENA')
linhas()
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {qtd} JOGOS  -=-=-=')
for i in range(0,qtd):
    lista.append(sorted(sample(range(1,61), k = 6)))
    print(f'Jogo {i+1}: {lista[i]}')
    sleep(1)
print(f'-=-=-=-=-=  < BOA SORTE! > -=-=-=-=-=')
