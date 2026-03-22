from datetime import date
a = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a%400 ==0:
    print(f'{a} é um ano bissexto!')
else:
    print(f'{a} não é um ano bissexto!')
