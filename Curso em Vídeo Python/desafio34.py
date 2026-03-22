s = float(input('qual o seu salário? '))
if s > 1250:
    sn1 = s + (s*10/100)
    print(f'seu novo salário, com um aumento de 10%, é {sn1:.2f}')
else:
    sn2 = s + (s * 15/100)
    print(f'seu novo salário, com um aumento de 15%, é {sn2:.2f}')
