a = 7
b = 2
c = a + b + 10
if c != 0:
    c += 1
for i in range(10000000) :
    c += 1      
print(f'Olá, c = {c*2}')
