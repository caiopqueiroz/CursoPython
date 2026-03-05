from urllib import request
import urllib

try:
    urllib.request.urlopen('http://www.pudim.com')
except:
    print('O site pudim não está acessível no momento :(')
else:
    print('Consegui acessar o site pudim! :)')