import os
def escreva(a):
    largura = os.get_terminal_size().columns
    texto_colorido = f"\033[{c1}m{a}{' ' * (largura - len(a))}\033[m"
    borda = f"\033[{c1}m{'~' * len(a)}{' ' * (largura - len(a))}\033[m"
    print(borda)
    print(texto_colorido)
    print(borda)
def ajuda():
    print(f'\033[7;{c1}m', end='')
    help(resp)
    print('\033[m', end='')
while True:
    c1 = 42
    escreva('SISTEMA DE AJUDA PyHELP')
    resp = str(input('Função ou Biblioteca > ')).lower().strip()
    if resp == 'fim':
        c1 = 41
        break
    else:
        c1 = 46
        escreva(f"Acessando o manual do comando '{resp}'")
        c1 = 48
        ajuda()
escreva('ATÉ LOGO!')
