import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site Pudim não esta ativo no momento')
else:
    print('O site pudim esta ativo no momento')
