v = float(input('digite a velocidade do carro em Km/h: '))
if v > 80:
    m = (v-80)*7
    print('você foi multado!')
    print('a multa vai custar R$7.00 por cada km acima do limite.')
    print(f'Sua multa: R${m:.2f}')



