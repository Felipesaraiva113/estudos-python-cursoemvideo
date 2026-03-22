import datetime
s = str(input('qual o seu sexo?[m/f] ')).lower()
if s == 'm':
    an = int(input('qual o seu ano de nascimento? '))
    a = datetime.date.today()
    d1 = a.year - an
    if d1 < 18:
        print(f'você ainda vai se alistar ao serviço militar, daqui a {18 - d1} anos.')
    elif d1 == 18:
        print('é hora de se alistar!')
    else:
        print(f'o tempo de se alistar já passou, há {d1 - 18} anos')
elif s =='f':
    print('sortuda...')