import pandas  # Importing the pandas library to handle CSV files

# Load the NATO phonetic alphabet data from a CSV file into a DataFrame
NATO_DATA = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the loaded data where each letter maps to its phonetic code
NATO_DICT = {row.letter: row.code for (index, row) in NATO_DATA.iterrows()}

def generate_phonetic():
    """Function to generate phonetic codes for each letter of the input word"""
    # Ask the user to input a word and convert it to uppercase
    question = input("Enter a word: ").upper()
    
    try:
        # Generate a list of phonetic codes for each letter in the input word
        output_list = [NATO_DICT[letter] for letter in question]
    except KeyError:
        # If a non-alphabetic character is entered, inform the user and re-prompt
        print("Sorry, only letters from the alphabet are allowed")
        generate_phonetic()  # Recursively call the function to ask for input again
    else:
        # Print the generated list of phonetic codes
        print(output_list)

# Call the function to execute
generate_phonetic()