s = str(input('Digite o seu sexo[M/F]: ')).upper().strip()
while s not in 'MF':
    s = str(input('Resposta inválida. Digite o seu sexo[M/F]: ')).strip().upper()
print('Resposta registrada com sucesso.')  