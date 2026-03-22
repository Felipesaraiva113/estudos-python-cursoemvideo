'''from math import factorial
n = int(input('digite um número: '))
print(f'{n}! = {factorial(n)}.')'''

n = int(input('digite um número: '))
sub = n
mult = n
while sub > 1:
    sub = sub - 1  
    mult = mult * sub
print(f'{n}! = {mult}.')
