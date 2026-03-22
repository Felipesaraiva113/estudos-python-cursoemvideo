n = s = c = 0
while True:
    n = int(input('digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    c += 1 
print(f'a soma dos {c} valores foi {s}!') 