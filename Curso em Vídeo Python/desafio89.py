boletim = []
name = []
notas = []
def linhas():
    print('-'*40)
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    name.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    name.append(notas[:])
    notas.clear()
    boletim.append(name[:])
    name.clear()
    sn = str(input('Quer continuar? [S/N] ')).strip().upper()
    if sn == 'N':
        break 
print('-='*40)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>6}')
print('-'*30)
for i in range(len(boletim)):
    m = sum(boletim[i][1])/2
    print(f'{i:<4}{boletim[i][0]:<15}{m:>6.1f}')
while True:
    linhas()
    pa = int(input('Mostrar notas de qual aluno? (999 interrompe): ' ))
    if pa == 999:
        break
    else:
        print(f'Notas de {boletim[pa][0]} são {boletim[pa][1]}')
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')    
