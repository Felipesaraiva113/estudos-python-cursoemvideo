from ex111.utilidades.dados import leiaInt
def linha(tam=42):
    return '-'*tam
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
def opçoes_categoria(lista):
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return int(opc)
def opçoes_materia(lista):
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[34m{i}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc
