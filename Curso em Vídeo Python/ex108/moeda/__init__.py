def metade(m):
    return m/2
def dobro(m):
    return m*2
def aumentar(m,n):
    a = m*n/100
    return m+a
def diminuir(m,n):
    a = m*n/100
    return m-a
def moeda(m):
    form = f'R${m:.2f}'.replace('.',',')
    return form