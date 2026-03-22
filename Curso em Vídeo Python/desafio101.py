from datetime import date
def voto(i):
    global idade
    if idade < 16:
        return 'NÃO VOTA.'
    elif 16<=idade < 18 or idade> 65:
        return 'VOTO OPCIONAL.'
    else:
        return 'VOTO OBRIGATÓRIO.'
print('-'*40)
nas = int(input('Em que ano você nasceu? '))
dty = date.today().year
idade = dty - nas
print(f'Com {idade} anos: {voto(nas)}')
