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
