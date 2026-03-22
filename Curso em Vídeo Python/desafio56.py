idade = []
sexo = []
idade_masculina = []
nome_masculino = []
totf = 0
contc = 30
for c in range(1,5):
    contc += 1   
    n = str(input(f'\033[{contc}mdigite o nome da {c}° pessoa: \033[m')).lower()
    i = int(input(f'\033[{contc}mdigite a idade da {c}° pessoa: \033[m'))
    idade.append(i)
    s = str(input(f'\033[{contc}mdigite o sexo da {c}° pessoa [m/f]: \033[m')).lower()
    sexo.append(s)
    print('')
    if s == 'm':
        idade_masculina.append(i)
        nome_masculino.append(n)
    if s == 'f':
        if i < 20:
            totf += 1
if idade_masculina:
    im = max(idade_masculina)
    indice = idade_masculina.index(im)
    nh = nome_masculino[indice]
    print(f'o homem mais velho do grupo é {nh}, com {im} anos de idade.')
mi = sum(idade)/len(idade)
print(f'média da idade do grupo: {mi:.1f}.')
print(f'{totf} mulheres têm menos de 20 anos.')





