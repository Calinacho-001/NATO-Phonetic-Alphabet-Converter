# NATO Phonetic Alphabet Converter

## Description

This is a Python script designed to convert a given word into its NATO phonetic alphabet equivalent. The project demonstrates the use of Python's `pandas` library for data handling and dictionary comprehension to create mappings. The updated script now includes error handling to ensure only alphabetic characters are entered and prompts the user for valid input if any non-alphabet characters are provided.

## Features

- **Data Processing**: Reads data from a CSV file containing the NATO phonetic alphabet.
- **Letter Conversion**: Converts user-inputted words into their phonetic alphabet equivalents.
- **Interactive Input**: Prompts the user to input a word for conversion.
- **Input Validation**: Ensures that the input contains only alphabetic characters, with error handling for invalid input.

## Requirements

- Python 3.x
- `pandas` library (install via `pip install pandas`)
- A CSV file named `nato_phonetic_alphabet.csv` containing the following format:

| letter | code       |
|--------|------------|
| A      | Alfa       |
| B      | Bravo      |
| C      | Charlie    |
| ...    | ...        |

## How to Use

<details>
<summary>Click here for detailed instructions</summary>

1. **Start the Application**:
   - Ensure the `nato_phonetic_alphabet.csv` file is in the same directory as the script.
   - Run the Python script using the provided command in the "How to Run" section.

2. **Input**:
   - Enter a word when prompted by the script. Only alphabetic characters will be processed.

3. **Functionality**:
   - The script will convert each letter of the entered word into its NATO phonetic alphabet equivalent and display the result.
   - If a non-alphabet character is entered, the script will prompt the user to enter a valid word.

</details>

## Code Structure

<details>
<summary>Click here for file breakdown</summary>

### `nato_phonetic_alphabet.csv`
- **Purpose**: Contains the NATO phonetic alphabet data in tabular form.
- **Columns**:
  - `letter`: The letter of the English alphabet.
  - `code`: The corresponding NATO phonetic code.

### `main.py`
- **Purpose**: Implements the logic to read the CSV file, map letters to phonetic codes, and prompt user input.
- **Key Functions**:
  - `generate_phonetic()`: Converts the user input to its NATO phonetic equivalent, with error handling for non-alphabetic characters.

</details>

## How to Run

1. Clone or download the project files, ensuring the `nato_phonetic_alphabet.csv` file is in the same directory as the script.
2. Execute the Python script using the following command:
    python main.py

3. Enter a word when prompted. The script will display the NATO phonetic code for each letter in the word.

## Future Improvements

<details>
<summary>Click here for possible future improvements</summary>

- **Improvement 1**: Add support for phrases or sentences instead of single words.
- **Improvement 2**: Develop a graphical user interface (GUI) for user-friendly interaction.

</details>

## Credits

This project was created as part of a Python learning exercise, focusing on data processing and dictionary comprehension.

## Change Log

<details>
<summary>Click here to view change log</summary>

### Version 1.1.0
- **Improved Input Validation**: Added recursive error handling for non-alphabetic characters. The script now asks the user to re-enter a valid word if invalid characters are entered.
  
### Version 1.0.0
- **Initial Release**: Converts user-inputted words into NATO phonetic alphabet equivalents.

</details>
