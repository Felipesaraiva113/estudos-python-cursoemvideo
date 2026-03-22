p = float(input('qual o seu peso? '))
a = float(input('qual a sua altura? '))
imc = p/(a**2)
if imc < 18.5:
    print('abaixo do peso.')
elif imc < 25:
    print('peso ideal.')
elif imc < 30:
    print('sobrepeso')
elif imc <= 40:
    print('obesidade.')
else:
    print('obesidade mórbida')