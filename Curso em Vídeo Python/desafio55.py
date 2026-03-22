pesos = []
for i in range(1,6):
    p = float(input(f'digite o peso da {i}° pessoa em kg: '))
    pesos.append(p)
maior = max(pesos)
menor = min(pesos)
print(f'o maior peso é {maior:.1f}kg e o menor é {menor:.1f}kg.')








