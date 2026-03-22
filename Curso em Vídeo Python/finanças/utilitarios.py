from categoria import Categoria
from transações import Transacao
lc = []
lt = []
def cc(nome):
    nc = Categoria(nome=nome) 
    lc.append(nc)
    return nc
def ct(d,v,c):
    nt = Transacao(descrição=d,valor=v,categoria=c) 
    lt.append(nt)
    return nt
def st():
    total = 0
    for t in lt:
        total += t.valor
    return total
     