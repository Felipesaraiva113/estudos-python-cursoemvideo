num = int(input('digite um número inteiro qualquer: '))
print('escolha uma das bases para conversão: ')
print('[1]converter para binpario ')
print('[2]converter para octal ')
print('[3]converter para hexadecimal ')
o = int(input('sua opção: '))
if o == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif o == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
else:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')