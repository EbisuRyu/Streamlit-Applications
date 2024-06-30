# Word Correction

This is a simple Streamlit word correction application that uses the Levenshtein distance algorithm to correct misspelled words.

## Features

- User input for misspelled words
- Suggests corrections based on the Levenshtein distance
- Interactive user interface for entering words and viewing corrections

## Prerequisites

- Python 3.8 or higher
- A dictionary file containing valid words (e.g., `vocab.txt`)

## How It Works

1. **User Input**: Enter a misspelled word in the input field. The application accepts the word and processes it to find the closest correct word.

2. **Calculate Levenshtein Distance**: The application uses the Levenshtein distance algorithm to calculate the distance between the input word and words in the dictionary.

3. **Suggest Correction**: Based on the calculated distances, the application suggests the closest correct word from the dictionary.

4. **Display Results**: The application displays the suggested correction along with the original input word, providing an interactive and user-friendly correction tool.

## Contributing

Feel free to contribute to this repository by opening issues or submitting pull requests.