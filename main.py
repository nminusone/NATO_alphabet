student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas as pd

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')
# print(type(phonetic_alphabet))

phonetic_dict = {row.letter: row.code for (index, row) in phonetic_alphabet.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input('Type your name to be phonetized:\n').upper()
user_list = list(user_input)
print(user_list)
#Angela's solution
output_list = [phonetic_dict[letter] for letter in user_input]
# My solution below
result = [value for char in user_list for (key, value) in phonetic_dict.items() if char == key]
print(result)
print(phonetic_dict)
