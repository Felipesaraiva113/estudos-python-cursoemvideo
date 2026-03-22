matriz = []
linhas = []
pares = []
sc = sp = 0
for l in range(0,3):       
    linhas = []
    for c in range(0,3):
        v = int(input(f'Digite um valor para [{l}, {c}]: '))
        linhas.append(v)
    matriz.append(linhas)          
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end=' ')
        if matriz[l][c] % 2 == 0:
            sp += matriz[l][c]
        if c == 2:
            sc += matriz[l][c]
    print()
sl = max(matriz[1])
print('-='*30)
print(f'A soma dos valores pares é {sp}')
print(f'A soma dos valores da terceira coluna é {sc}')
print(f'O maior valor da segunda linha é {sl}')

