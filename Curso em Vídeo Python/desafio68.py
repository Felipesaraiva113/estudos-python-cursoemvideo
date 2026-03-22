from random import randint
def linhas_igual():
    print('=-' * 15)
def linhas():
    print('-' * 15)
linhas_igual()
print('VAMOS JOGAR PAR OU ÍMPAR')
linhas_igual()
sv = 0
while True:
    vj = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    vc = randint(0,10)
    s = vc + vj
    linhas()
    print(f'Você jogou {vj} e o computador {vc}. Total de {s}', end= ' ')
    if s % 2 == 0: 
        print('DEU PAR')
        resultado = 'P'
    else:
        print('DEU ÍMPAR')
        resultado = 'I'
    linhas()
    if pi == resultado:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        linhas_igual()
        sv += 1
    else:
        print('VOCÊ PERDEU!')
        linhas_igual()
        print(f'GAME OVER! Você venceu {sv} vezes.')
        break
