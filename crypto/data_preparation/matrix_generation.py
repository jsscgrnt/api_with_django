import string 

import numpy as np

class cleaning_data():

    def __init__(self, input_word: str) -> None:
        self.input_word = input_word

    def change_y_for_i(self):
        return self.input_word.replace("Y", "I")
    
    def ignore_duplicated(self):
        return "".join(dict.fromkeys(self.input_word))

class generate_final_order():

    alphabet_list = list(string.ascii_uppercase)

    def __init__(self) -> None:
        pass

    def sort_words(self, key_word: str):
        self.key_word = key_word
        self.alphabet_modified = self.alphabet_list[:]
        for i in range(len(self.key_word)):
            self.alphabet_modified.insert(i, self.key_word[i])
        return self.alphabet_modified
    
    def sorted_letter_matrix(self, alphabet_modified):
        self.letter_matrix = np.array(list(alphabet_modified))
        self.letter_matrix = self.letter_matrix.reshape(5,5)
        return self.letter_matrix

    def key_position_in_alphabet_matrix(self, letter_matrix, encrypto_word: str):
        self.letter_matrix = letter_matrix
        self.encrypto_word = encrypto_word
        self.final_coord = ""
        for letter in self.encrypto_word:
            index = np.where(self.letter_matrix == letter)
            x_axis = index[0][0]
            y_axis = index[1][0]
            self.final_coord = f"{self.final_coord}{x_axis}{y_axis}"
        return self.final_coord
        