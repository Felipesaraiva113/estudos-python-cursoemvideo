a1 = int(input('digite o primeiro termo da PA: '))
r = int(input('digite a razão: '))
p = a1 + (10 - 1)*r
for c in range(a1,p+r, r):
    print(c, end=' ')