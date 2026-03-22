def poi(a):
    if a % 2 ==0:
        print(f'{a} é um número par!')
    else: 
        print(f'{a} é um número ímpar!')

num = int(input('digite um número inteiro: '))
poi(num)
