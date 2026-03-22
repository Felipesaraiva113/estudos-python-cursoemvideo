def linhas():
    print('-' * 30)
while True:
    n = int(input('\033[31mquer ver a tabuada de qual valor? \033[m'))
    linhas()
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\033[32m{n}\033[m \033[34mx\033[m \033[33m{c:2}\033[m \033[36m=\033[m \033[35m{n*c}\033[m')
    linhas()
print('programa T.A.B.U.A.D.A encerrado.')
print('volte sempre!')