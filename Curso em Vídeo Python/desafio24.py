c = str(input('didite o nome de uma cidade: ')).strip()
if c[:5].upper() == 'SANTO':
    print('A cidade começa com "Santo"')
else:
    print('A cidade não começa com "Santo"')