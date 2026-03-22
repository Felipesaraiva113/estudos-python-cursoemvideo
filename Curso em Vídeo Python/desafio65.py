i = 0
r2 = 's'
r1 = 0
n = []
while r2 != 'n':
    r1 = int(input('digite um número inteiro qualquer: '))
    n.append(r1)
    r2 = str(input('quer continuar? [s/n] ')).lower().strip()
qtd = len(n)
m = sum(n)/qtd
print(f'você digitou {qtd} números e a média foi {m:.2f}')
print(f'o maior valor foi {max(n)} e o menor foi {min(n)}')

