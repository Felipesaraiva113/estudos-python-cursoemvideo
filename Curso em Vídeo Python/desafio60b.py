n = int(input('digite um número: '))
n2 = n
mult = n
for c in range(n,0,-1):
    n2 = n2 - 1
    if n2 > 0:
        mult = mult * n2
print(f'\033[31m{n}! = {mult} \033[m')