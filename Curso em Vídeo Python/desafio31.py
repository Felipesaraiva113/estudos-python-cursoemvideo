d = float(input('qual a distância da sua viagem em Km? '))
if d <= 200:
   print(f'o preço da passagem será R${d*0.5:.2f}') 
else:
  print(f'o preço da passagem será R${d*0.45:.2f}') 