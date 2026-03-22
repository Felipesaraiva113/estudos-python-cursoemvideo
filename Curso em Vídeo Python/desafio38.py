n1 = int(input('digite um número inteiro: '))
n2 = int(input('digite outro: '))
if n1 < n2:
    maior = n2
    print(f'maior número: {maior}')
elif n2 < n1:
    maior = n1
    print(f'maior número: {maior}')
else:
    print('não existe valor maior, os dois são iguais.')
    


    
