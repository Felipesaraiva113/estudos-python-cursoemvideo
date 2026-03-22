from random import randint
from time import sleep
def sorteio(lst):
    print('Sorteando 5 valores da lista:',end=' ')
    for i in range(1,6):
        srt = randint(1,5)
        print(srt, end=' ', flush=True)
        sleep(0.5)
        lista.append(srt)
    print('PRONTO!')
lista = []
def soma():
    sp = 0
    for p in lista:
        if p%2==0:
            sp += p
    print(f'Somando os valores pares de {lista}, temos {sp}')
sorteio(lista)
soma()
