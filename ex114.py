import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.github.com')
except urllib.error.URLError:
    print('O site Github não está acessivel nomomento')
else:
    print('Consegui acessar o site do Github com sucesso')
    print(site.read())