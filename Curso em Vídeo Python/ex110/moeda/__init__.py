def metade(m,form=False):
    if form == True:
        return moeda(m/2)
    else:
        return m/2
def dobro(m,form=False):
    if form == True:
        return moeda(m*2)
    else:
        return m*2
def aumentar(m,n,form=False):
    a = m*n/100
    if form == True:
        return moeda(m+a)
    else:
        return m+a
def diminuir(m,n,form=False):
    a = m*n/100
    if form == True:
        return moeda(m-a)
    else:
        return m-a
def moeda(m):
    form = f'R${m:.2f}'.replace('.',',')
    return form
def resumo(m,au,re):
    def linhas():
        print('-'*30)
    linhas()
    print('RESUMO DO VALOR'.center(30))
    linhas()
    print(f'Preço analisado: \t{moeda(m)}')
    print(f'Dobro do preço: \t{dobro(m,True)}')
    print(f'Metade do preço: \t{metade(m,True)}')
    print(f'{au}% de aumento: \t{aumentar(m,au,True)}')
    print(f'{re}% de redução: \t{diminuir(m,re,True)}')
    linhas() 
