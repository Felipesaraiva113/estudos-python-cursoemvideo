n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('aluno reprovado.')
elif m >= 5 and  m <= 6.9:
    print('aluno de recuperação.')
else: 
    print('aluno aprovado.')

