n1 = float(input('digite um número: '))
n2 = float(input('digite outro número: '))
n3 = float(input('digite o último número: '))
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
print(f'menor número: {menor}')
print(f'maior número: {maior}')




 

