import requests 
r=requests.get('https://ipinfo.io/json')
t = r.json()
print(f'Seu IP: {t["ip"]}')
print(f'Cidade: {t["city"]}')
print(f'Estado: {t["region"]}')
print(f'País: {t["country"]}')
print(f'Provedor: {t["org"]}')