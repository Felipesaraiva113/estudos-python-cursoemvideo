from time import sleep
def linhas():
    print('-='*30)
def contador(a,b,c):
    linhas()
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    if b < a and c > 0:
        b = b-c
        c = -c
    elif c < 0:
        b = b-1
    elif c == 0:
        b -= 1
        c = -1
    else:
        b = b + 1
    for i in range(a,b,c):
        print(i, end=' ',flush=True)
        sleep(0.5)
    print('FIM!')
contador(1,10,1)
contador(10,0,-2)
linhas()
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')),int(input('Fim: ')),int(input('Passo: ')))
