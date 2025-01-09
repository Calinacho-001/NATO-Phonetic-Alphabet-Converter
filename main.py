import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

question = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in question]
print(output_list)
