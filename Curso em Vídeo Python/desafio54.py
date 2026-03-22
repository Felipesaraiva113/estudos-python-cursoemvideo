from datetime import date
cma = 0
cme = 0
ay = date.today().year
for i in range(1,8):
    a = int(input('digite seu ano de nascimento: '))
    idade = ay - a
    if idade >= 18:
        cma += 1
    else:
        cme += 1
print(f'{cme} pessoas ainda não atingiram a maioridade.')
print(f'{cma} pessoas já atingiram a maioridade.')
