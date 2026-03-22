def fatorial(num,show=False):
    f = 1
    for c in range(num, 0, -1):
        f *=c 
        if show == True:
            if c != 1:
                xig = 'x'
            else:
                xig = '='
            print(f'{c} {xig}', end=' ')
    return f
print('-'*40)
f1 = fatorial(5,show=True)
print(f1)
