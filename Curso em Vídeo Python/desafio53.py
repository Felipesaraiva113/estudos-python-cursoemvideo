import unidecode
f = str(input('escreva uma frase: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('a frase é um palíndromo.')
else:
     print('a frase não é um palíndromo.')


