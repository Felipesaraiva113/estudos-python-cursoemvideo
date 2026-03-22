c = 0
n = int(input('digite um número inteiro: '))
for i in range(1,n+1):
    if n % i == 0:
        c += 1
if c==2:
    print(f'o número inteiro {n} é primo.')
else:
    print(f'o número inteiro {n} não é primo.')



    
