import requests
try:
    resposta = requests.get('https://www.google.com')
    resposta.raise_for_status()
except requests.exceptions.RequestException:
    print('O site Google não está acessível no momento.')
else:
    print('Consegui acessar o site Google com sucesso.')
