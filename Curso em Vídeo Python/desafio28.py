from random import randint
e = randint(0,10)
c = 0
r = int(input('Pensei em um número inteiro entre 0 e 10. Tente descobrir qual é: '))
c +=1
while e != r:
    print('hehe')
    r = int(input('Você errou. Tente novamente: '))
    c +=1
print(f'Parabéns, você acertou! Foram necessárias {c} tentativas!')
