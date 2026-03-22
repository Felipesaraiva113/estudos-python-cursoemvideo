import requests 
c=str(input('Digite um CEP: '))
r=requests.get(f'https://viacep.com.br/ws/{c}/json/')
t = r.json()
print(f"Rua: {t['logradouro']}")
print(f"Bairro: {t['bairro']}")
print(f"Cidade: {t['localidade']}")
print(f"Estado: {t['uf']}")
