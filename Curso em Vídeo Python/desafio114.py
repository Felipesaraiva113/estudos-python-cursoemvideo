import urllib
import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print('O site Google não está acessível no momento.')
else:
    print('Consegui acessar o site Google com sucesso.')
