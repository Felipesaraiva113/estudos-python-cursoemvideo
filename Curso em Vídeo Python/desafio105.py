def notas(*n, sit = False):
    dicionario = {}
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['média'] = sum(n)/len(n)
    if sit == True:
        if dicionario['média'] >= 7:
            dicionario['situação'] = 'BOA'
        elif dicionario['média'] >= 6:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'    
    return dicionario
resp = notas(5.9,9.5,10,6.5, sit = True)
print(resp)
