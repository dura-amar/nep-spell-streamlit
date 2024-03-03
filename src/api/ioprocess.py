import json
import re

def diff(str1, str2):
    indices = []
    words1 = str1.split()
    words2 = str2.split()

    for index, (word1, word2) in enumerate(zip(words1, words2)):
        if word1 != word2:
            start_index = sum(
                len(word) + 1 for word in words1[:index]
            )  # Add 1 for the space between words
            indices.append((start_index, start_index + len(word1)))

    # If str2 has more words than str1, record the indices of the extra words in str2
    for index in range(len(words1), len(words2)):
        start_index = sum(
            len(word) + 1 for word in words1
        )  # Add 1 for the space between words
        indices.append((start_index, start_index + len(words2[index])))

    return indices


def format_predicted_sentence(original_sentence, corrected_word_indices):
    formatted_sentence = ""
    current_index = 0

    for start_index, end_index in corrected_word_indices:
        # Add the part of the sentence before the corrected word
        formatted_sentence += original_sentence[current_index:start_index]

        # Add the corrected word wrapped in a span
        formatted_sentence += (
            '<span style="color:red">'
            + original_sentence[start_index : end_index + 1]
            + "</span>"
        )

        # Update the current index
        current_index = end_index + 1

    # Add the remaining part of the sentence
    formatted_sentence += original_sentence[current_index:]

    return formatted_sentence


def processInputAndResults(inputSentence, predictedSentence):
    corrected_word_indices = diff(inputSentence, predictedSentence)
    formatted_sentence = format_predicted_sentence(
        predictedSentence, corrected_word_indices
    )
    return formatted_sentence


def ensure_space_around_punctuation(sentence):
    punctuation_marks = ["।", ",", ".", "!", "?", ":", ";", '"', "'", "(", ")"]
    for mark in punctuation_marks:
        index = sentence.find(mark)
        while index != -1:
            # Ensure space before the punctuation mark
            if index > 0 and sentence[index - 1] != " ":
                sentence = sentence[:index] + " " + sentence[index:]
                index += 1  # Adjust index due to inserted space
            # Ensure space after the punctuation mark
            if index < len(sentence) - 1 and sentence[index + 1] != " ":
                sentence = sentence[: index + 1] + " " + sentence[index + 1 :]
                index += 1  # Adjust index due to inserted space
            # Find next occurrence of the punctuation mark
            index = sentence.find(mark, index + 1)
    return sentence


def check_and_insert_space(sentence):
    index = sentence.find("।")  # Find the index of "।"
    if index > 0 and sentence[index - 1] != " ":
        sentence = sentence[:index] + " " + sentence[index:]  # Insert space before "।"
    return sentence

def processPunctuation(sentence):
    # Define a regex pattern to match punctuation marks
    punctuation_pattern = r'([।,\.!\?:;"\'\(\)])'
    
    # Use re.sub() to replace punctuation marks with themselves surrounded by spaces
    # The pattern matches any punctuation mark and replaces it with " <punctuation_mark> "
    modified_sentence = re.sub(punctuation_pattern, r' \1 ', sentence)
    
    # Replace any occurrences of double spaces with single spaces
    modified_sentence = re.sub(r'\s+', ' ', modified_sentence)
    
    return modified_sentence