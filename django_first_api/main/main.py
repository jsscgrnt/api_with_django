import requests

host = 'http://127.0.0.1:8000'
service = '/alunos/'

r = requests.get(f'{host}{service}')

pload = {'nome':'mia', 'rg':'456465'}
r = requests.post(f'{host}{service}', data = pload)

print(r)
