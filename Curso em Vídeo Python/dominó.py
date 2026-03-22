pares = {"3x4": "12","2+5": "7","5+1": "6", "6/3": "2"} 
alt = 0
while True:
    if alt%2 ==0:
        jog = 1
    else:
        jog = 2
    p1 = str(input(f'jogador {jog} informe a operação: ')).strip()
    p2 = str(input(f'jogador {jog} informe o resultado: ')).strip()
    if pares[p1] == p2: 
        print('combinação válida!')  
        alt += 1
        sn = str(input('quer continuar? [s/n] ')).strip().lower()
        if sn == 'n':
            break
    else:
        print('combinação inválida!')
        resp = str(input('você tem uma peça jogável? [s/n] ')).strip().lower()
        if resp == 'n':
            alt += 1
   
    