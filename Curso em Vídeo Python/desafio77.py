palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro', 'esforço')
vogais = ('a', 'e', 'i', 'o', 'u')

for i in palavras:
    print(f'Na palavra {i.upper()} temos ', end=' ')
    for letras in i:
        if letras in vogais:
            print(letras, end=' ')
    print()

