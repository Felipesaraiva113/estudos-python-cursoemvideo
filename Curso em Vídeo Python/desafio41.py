from datetime import date
an = int(input('digite o ano de nascimento de um atleta: '))
a = date.today().year
i = a - an
if i <= 9:
    print('ele(a) tem até 9 anos de idade, logo ele pertence a categoria: mirim.')
elif i <= 14:
    print('ele(a) tem até 14 anos de idade, logo ele pertence a categoria: infantil.')
elif i <= 19:
    print('ele(a) tem até 19 anos de idade, logo ele pertence a categoria: júnior.')
elif i <= 25:
    print('ele(a) tem até 25 anos de idade, logo ele pertence a categoria: sênior.')
else:
    print('ele(a) tem mais de 25 anos de idade, logo ele pertence a categoria: master.')