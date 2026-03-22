n = input('qual o seu nome? ')
print(f'olá {n}, meu nome é bqvqtrpfut-1, o seu bot que verifica quando três retas podem formar um triangulo-1')
r1 = float(input('digite o comprimento da primeira reta: '))
r2 = float(input('digite o comprimento da segunda reta: '))
r3 = float(input('digite o comprimento da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('as três retas que você digitou podem formar um triângulo.')
    if r1 == r2  == r3:
        print('triângulo equilátero: todos os lados são iguais.')
    elif r1 == r2 or r1==r3 or r2 == r3:
        print('triângulo isóceles: dois lados iguais.')
    else:
        print('triângulo escaleno: todos os lados diferentes.')
else:
    print('as três retas que você digitou não podem formar um triângulo.')
   
