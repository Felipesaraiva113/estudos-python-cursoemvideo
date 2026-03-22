v = float(input('qual o valor da casa que pretende financiar? '))
s = float(input('qual o seu salário? '))
a = float(input('e em quantos anos pretende pagar? '))
p = v/(a*12)
if p <= s*30/100:
    print('empréstimo aprovado!')
    print(f'o valor da prestação mensal será {p:.2f}')
else:
    print('empréstimo negado.')
    print(f'o valor da prestação mensal será {p:.2f}')