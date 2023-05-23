# -------------------------------------------------------------------
# Project:    Wordle-Scoring
#
# Filename:   score_word.py
# Location:   ./src
#
# Author:     Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created:    21/5/2023
#
# Purpose:
#    This file provides the following features, methods and associated 
#    supporting code:
#
#    get_letter_scores(word: str, guess: str) -> list
#    
# ---------------------------------------------------------------------

def get_letter_scores(word: str, guess: str) -> list:
    """
    This function takes two words and compares them, returning a list of
    scores for each letter in the word.
    The scores are:
        0 - the letter is not in the word
        1 - the letter is in the word, but not in the correct position
        2 - the letter is in the word, and in the correct position


    :param word: string containing the word to be guessed
    :param guess: string containing the word guessed
    :return: list of scores for each letter in the word
    """

    w_len = len(word)  # get the length of the word
    g_len = len(guess)  # get the length of the guess

    # check if the word and guess are the same length
    # if they are not, raise a ValueError
    if w_len != g_len:
        raise ValueError("The word and guess must be the same length")

    # check if the word and guess are the same
    # if they are, return a list of 2s
    if word == guess:
        return [2] * w_len

    # initialise the result list
    result = [0] * w_len

    # convert the word and guess to lists
    word_list = list(word)
    guess_list = list(guess)

    # check for exact matches
    for word_pos in range(w_len):
        # check if the letter in the word is the same as the letter in
        # the guess, and if it is, set the result to 2
        if word_list[word_pos] == guess_list[word_pos]:
            result[word_pos] = 2
            word_list[word_pos] = " "
            guess_list[word_pos] = " "

    # check for partial matches
    for word_pos in range(w_len):

        # check if the letter in the word is in the guess
        if word_list[word_pos] not in [" ", None]:
            # if it is, check if it is in the guess
            for guess_pos in range(w_len):
                # if it is, set the result to 1
                # and remove the letter from the word and guess
                if guess_list[guess_pos] == word_list[word_pos]:
                    result[guess_pos] = 1
                    word_list[word_pos] = " "
                    guess_list[guess_pos] = " "
                    break

    # return the resulting list of scores
    return result
