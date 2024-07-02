import streamlit as st
import numpy as np


def load_vocab(file_path):
    """
    Load vocabulary from a file and return a sorted list of unique words.

    Args:
        file_path (str): Path to the vocabulary file.

    Returns:
        list: A sorted list of unique words.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    words = sorted(set([line.strip() for line in lines]))
    return words


def levenshtein_distance(source: str, target: str):
    """
    Calculates the Levenshtein distance between two strings.

    The Levenshtein distance is a metric for measuring the difference between
    two sequences. It is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one word into the other.

    Args:
        source (str): The source string.
        target (str): The target string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """

    # Length of the source and target strings + 1 for the matrix dimensions
    delete_len = len(source) + 1
    insert_len = len(target) + 1

    # Initialize the distance matrix with the appropriate shape
    distance_matrix = np.ndarray(
        shape=(delete_len, insert_len), dtype=np.uint8)

    # Initialize the first column and first row of the matrix
    distance_matrix[:, 0] = np.arange(delete_len, dtype=np.uint8)
    distance_matrix[0, :] = np.arange(insert_len, dtype=np.uint8)

    def distance_matrix_element_computing(delete_axis, insert_axis):
        """
        Computes the value for a given cell in the distance matrix.

        Args:
            delete_axis (int): The current row index in the distance matrix.
            insert_axis (int): The current column index in the distance matrix.

        Returns:
            int: The computed value for the cell.
        """
        # Compute the possible values from neighboring cells
        candidate_1 = distance_matrix[delete_axis -
                                      1][insert_axis] + 1  # Deletion
        # Insertion
        candidate_2 = distance_matrix[delete_axis][insert_axis - 1] + 1
        sub_cost = 0 if target[insert_axis -
                               # Substitution
                               1] == source[delete_axis - 1] else 1
        candidate_3 = distance_matrix[delete_axis -
                                      # Substitution or match
                                      1][insert_axis - 1] + sub_cost

        # Return the minimum of the three candidates
        return min(candidate_1, candidate_2, candidate_3)

    # Fill in the rest of the distance matrix
    for delete_axis in range(1, delete_len):
        for insert_axis in range(1, insert_len):
            distance_matrix[delete_axis][insert_axis] = distance_matrix_element_computing(
                delete_axis, insert_axis)

    return distance_matrix[delete_len - 1][insert_len - 1]


def main():
    """
    Main function to run the Streamlit application for word correction using Levenshtein distance.
    """
    # Load vocabulary from the specified file
    vocabs = load_vocab(file_path='./Word-Correction/vocab.txt')

    # Set the title of the Streamlit app
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word: ")  # Input field for the word to correct

    if st.button("Compute"):
        # Compute Levenshtein distances between the input word and all vocabulary words
        levenshtein_distances = dict()
        for vocab in vocabs:
            levenshtein_distances[vocab] = levenshtein_distance(word, vocab)

        # Sort the distances and find the word with the smallest distance
        sorted_distances = dict(
            sorted(levenshtein_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]

        # Display the corrected word
        st.markdown(f"#### Correct Word: {correct_word}")

        # Display vocabulary and distances in two columns
        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
