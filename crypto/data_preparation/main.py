from matrix_generation import *

chave = 'MSZHWQLFNREIQUQLAMDGXOKAP'
palavra = 'JESSICA'

teste = generate_final_order().sort_words(chave)
teste = ''.join(teste)
# print(teste)
# print('\n')

teste2 = cleaning_data(teste).change_y_for_i()
# print(teste2)
# print('\n')

teste3 = cleaning_data(teste2).ignore_duplicated()
# print(teste3)
# print(len(teste3))
# print('\n')

teste4 = generate_final_order().sorted_letter_matrix(teste3)
print(teste4)
print('\n')

teste5 = generate_final_order().key_position_in_alphabet_matrix(letter_matrix= teste4, encrypto_word=palavra)
print(teste5)