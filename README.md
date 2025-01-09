# NATO Phonetic Alphabet Converter

## Description

This is a Python script designed to convert a given word into its NATO phonetic alphabet equivalent. The project demonstrates the use of Python's `pandas` library for data handling and dictionary comprehension to create mappings.

## Features

- **Data Processing**: Reads data from a CSV file containing the NATO phonetic alphabet.
- **Letter Conversion**: Converts user-inputted words into their phonetic alphabet equivalents.
- **Interactive Input**: Prompts the user to input a word for conversion.

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
   - Enter a word when prompted by the script.

3. **Functionality**:
   - The script will convert each letter of the entered word into its NATO phonetic alphabet equivalent and display the result.

</details>

## Code Structure

<details>
<summary>Click here for file breakdown</summary>

### `nato_phonetic_alphabet.csv`
- **Purpose**: Contains the NATO phonetic alphabet data in tabular form.
- **Columns**:
  - `letter`: The letter of the English alphabet.
  - `code`: The corresponding NATO phonetic code.

### `script_name.py`
- **Purpose**: Implements the logic to read the CSV file, map letters to phonetic codes, and prompt user input.
- **Key Functions**:
  - Dictionary comprehension to create a letter-to-code mapping.
  - List comprehension to transform user-inputted words into phonetic codes.

</details>

## How to Run

1. Clone or download the project files, ensuring the `nato_phonetic_alphabet.csv` file is in the same directory as the script.
2. Execute the Python script using the following command:
    ```bash
   python script_name.py  
    ```

3. Enter a word when prompted. The script will display the NATO phonetic code for each letter in the word.

## Future Improvements

<details>
<summary>Click here for possible future improvements</summary>

- **Improvement 1**: Add error handling for non-alphabetic characters.
- **Improvement 2**: Support for phrases or sentences instead of single words.
- **Improvement 3**: Develop a graphical user interface (GUI) for user-friendly interaction.

</details>

## Credits

This project was created as part of a Python learning exercise, focusing on data processing and dictionary comprehension.

## Change Log

<details>
<summary>Click here to view change log</summary>

### Version 1.0.0
- **Initial Release**: Converts user-inputted words into NATO phonetic alphabet equivalents.

</details>
