n1 = float(input('digite um número: '))
n2 = float(input('digite um número: '))
def menu():
    print('')
    print('[1] somar.')
    print('[2] multiplicar.')
    print('[3] maior.')
    print('[4] novos números.')
    print('[5] sair do programa.')
    print('')
r = 0
while r != 5:
    menu()
    r = int(input('informe sua escolha: '))
    if r == 1:
        print(f'a soma entre os valores digitados é {n1 + n2:.2f}')       
    elif r == 2:
        print(f'a multiplicação entre os valores digitados é {n1 * n2:.2f}')    
    elif r == 3:
        print(f'o maior valor digitado foi: {max(n1, n2)}')    
    elif r == 4:
        n1 = float(input('digite um número: '))
        n2 = float(input('digite um número: '))
        
    





        
