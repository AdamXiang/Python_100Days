student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows() 只有在Dataframe才可以用
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
table = pandas.read_csv("nato_phonetic_alphabet.csv")
phone_dict = {row["letter"]:row["code"] for (index, row) in table.iterrows() if row[0] != "letter"}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# 作法一
# is_correct = True
# name = input("Enter a word: ").upper()
# while is_correct:
#     try:
#         #  loop name，要把dict中，name裡的letter抽取出來
#         result = [phone_dict[letter] for letter in name]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         name = input("Enter a word: ").upper()
#     else:
#         is_correct = False

# 作法二
def generate_phonetic():
    name = input("Enter a word: ").upper()
    try:
        #  loop name，要把dict中，name裡的letter抽取出來
        result = [phone_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)
# al_list = []
# for letter in name:
#     for key in phone_dict.values():
#         if letter in key[0]:
#             al_list.append(key)
#
generate_phonetic()