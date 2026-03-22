import requests
u = str(input('Digite a URL do site: '))
r = requests.get(u)
if r.status_code == 200:
    print('O site está no ar!',end=' ')
else:
    print('O site pode estar fora do ar',end=' ')
print(f'(Código: {r.status_code})')
