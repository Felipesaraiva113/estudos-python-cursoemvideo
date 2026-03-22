vnormal = float(input('qual o valor do produto? '))
print('[pressione 1 se vai pagar à vista com dinheiro/cheque]')
print('[pressione 2 se vai pagar à vista no cartão]')
print('[pressione 3 se vai pagar em até 2 vezes no cartão]')
print('[pressione 4 se vai pagar 3 vezes ou mais no cartão]')
p = (input('qual a sua escolha? '))
match p:
    case '1':
        print(f'novo valor, com desconto de 10%: R${vnormal-(10*vnormal/100):.2f}.')
    case '2':
        print(f'novo valor, com desconto de 5%: R${vnormal-(5*vnormal/100):.2f}.')
    case '3':
        print(f'o valor continua sendo R${vnormal}.')
    case '4':
        print(f'novo valor, com juros de 20%: R${vnormal+(20*vnormal/100):.2f}.')

