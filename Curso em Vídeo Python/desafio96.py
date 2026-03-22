def area(b,h):
    a = b*h 
    print(f'A área de um terreno de {b}x{h} é de {a}m².')    
print('  Controle de Terrenos')
print('-'*20)
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
