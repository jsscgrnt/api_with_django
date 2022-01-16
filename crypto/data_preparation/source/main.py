import requests
from matrix_generation import *

host = 'http://127.0.0.1:8000'
service = '/crypto/'

chave = "MSZHWQLFNREIQUQLAMDGXOKAP"
palavra = "JESSICA"

teste = generate_final_order().sort_words(chave)
teste = ''.join(teste)
teste2 = cleaning_data(teste).change_y_for_i()
teste3 = cleaning_data(teste2).ignore_duplicated()
teste4 = generate_final_order().sorted_letter_matrix(teste3)
teste5 = generate_final_order().key_position_in_alphabet_matrix(letter_matrix= teste4, encrypto_word=palavra)

palavra_encriptada = teste5

pload = {"chave":chave,"palavra":palavra,"palavra_encriptada":palavra_encriptada}
r = requests.post(f'{host}{service}', data = pload)
print(r)

r = requests.get(f'{host}{service}')
print(r.text)
