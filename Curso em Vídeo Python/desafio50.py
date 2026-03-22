s = 0
for c in range(6):
    n = int(input('digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print(f'a soma entre os números pares digitados é {s}')
