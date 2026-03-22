n = int(input('digite um número de 0 a 9999: '))
u = n // 1 % 10 
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')