def igual():
    print('='*30)
igual()
print('          SANTANDER')
igual()
v = int(input('Que valor você quer sacar? R$'))
total = v
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} células de R${ced}')  
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
igual()
print('Volte sempre ao SANTANDER! Tenha um bom dia!')


