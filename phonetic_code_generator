# Phonetic code words generator
import pandas


data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dictionary = {row.letter: row.code for (index, row) in data_frame.iterrows()}
letter_list = list(input('What\'s you name?: ').upper())

phonetic_code_words_list = [phonetic_dictionary[letter] for letter in letter_list]
print(phonetic_code_words_list)
