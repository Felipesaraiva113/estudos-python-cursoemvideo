estado = dict()
brasil = list()
for c in range(0,1):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
