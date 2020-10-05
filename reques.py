import requests

a = requests.get('http://www.colegiosion.com.br/')

print(a.headers)
