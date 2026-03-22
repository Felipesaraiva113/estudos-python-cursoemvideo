n = int(input('\033[4;31mdigite um número inteiro: \033[m'))
for c in range(1, 11):
 print(f'\033[32m{n}\033[m \033[34mx\033[m \033[33m{c:2}\033[m \033[36m=\033[m \033[35m{n*c}\033[m')