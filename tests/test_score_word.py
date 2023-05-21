# -------------------------------------------------------------------
# Project:    Wordle-Scoring
# Filename:   test_score_word.py
# Location:   ./tests
# Author:     Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created:    21/5/2023
# Purpose:
#    This file provides the following features, methods and associated 
#    supporting code:
#    
# ---------------------------------------------------------------------
import unittest

from src.score_word import get_letter_scores


class MyTestCase(unittest.TestCase):
    def words(self, word_one: str, word_two: str) -> str:
        """
        Helper function to return the words being tested

        :param word_one: 
        :param word_two: 
        
        :return: string containing the words in form "word_one, 
        word_two"
        """
        return f"{word_one}, {word_two}"

    def test_word_hello_spams(self) -> None:
        """
        Test case -  word: hello, guess: spams, [0,0,0,0,0]
        :return:  None
        """
        guess = "spams"
        word = "hello"
        result = [0, 0, 0, 0, 0]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_nears_saner(self) -> None:
        """
        Test case -  word: nears, guess: saner, [1,1,1,1,1]
        
        :return:  None
        """
        guess = "saner"
        word = "nears"
        result = [1, 1, 1, 1, 1]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_hello_hello(self) -> None:
        """
        Test case -  word: hello, guess: hello, [2,2,2,2,2]
        
        :return:  None
        """
        guess = "hello"
        word = "hello"
        result = [2, 2, 2, 2, 2]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_petal_level(self) -> None:
        """
        Test case -  word: petal, guess: level, [0,2,0,0,2]
        
        :return:  None
        """
        guess = "level"
        word = "petal"
        result = [0, 2, 0, 0, 2]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_erect_melee(self) -> None:
        """
        Test case -  word: erect, guess: melee, [0,1,0,1,0]
        
        :return:  None
        """
        guess = "melee"
        word = "erect"
        result = [0, 1, 0, 1, 0]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_relit_tiler(self) -> None:
        """
        Test case -  word: relit, guess: tiler, [1,1,2,1,1]
        
        :return: None
        """
        guess = "tiler"
        word = "relit"
        result = [1, 1, 2, 1, 1]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_bores_sober(self) -> None:
        """
        Test case -  word: bores, guess: sober, [1,2,1,2,1]
        :return: None
        """
        guess = "sober"
        word = "bores"
        result = [1, 2, 1, 2, 1]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_bores_robes(self) -> None:
        """
        Test case -  word: bores, guess: robes, [1,2,1,2,2]
        
        :return: None 
        """
        guess = "robes"
        word = "bores"
        result = [1, 2, 1, 2, 2]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_tyres_stray(self) -> None:
        """
        Test case -  word: tyres, guess: stray, [1,1,2,0,1]
        
        :return:  None
        """
        guess = "stray"
        word = "tyres"
        result = [1, 1, 2, 0, 1]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_evens_every(self) -> None:
        """
        Test case -  word: evens, guess: every, [2,2,2,0,0]
        
        :return:  None
        """
        guess = "every"
        word = "evens"
        result = [2, 2, 2, 0, 0]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_minor_major(self) -> None:
        """
        Test case -  word: minor, guess: major, [2,0,0,2,2]
        :return:  None
        """
        guess = "major"
        word = "minor"
        result = [2, 0, 0, 2, 2]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_train_inter(self) -> None:
        """
        Test case -  word: train, guess: inter, [1,1,1,0,1]
        
        :return:  None
        """
        guess = "inter"
        word = "train"
        result = [1, 1, 1, 0, 1]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_array_sprat(self) -> None:
        """
        Test case -  word: array, guess: sprat, [0,0,2,2,0]
        
        :return:  None
        """
        guess = "sprat"
        word = "array"
        result = [0, 0, 2, 2, 0]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_melee_meter(self) -> None:
        """
        Test case -  word: melee, guess: meter, [2,2,0,2,0]
        
        :return:  None
        """
        guess = "meter"
        word = "melee"
        result = [2, 2, 0, 2, 0]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_alloy_lorry(self) -> None:
        """
        Test case -  word: alloy, guess: lorry, [1,1,0,0,2]
        
        :return:  None
        """
        guess = "lorry"
        word = "alloy"
        result = [1, 1, 0, 0, 2]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_alloy_spray(self) -> None:
        """
        Test case -  word: alloy, guess: spray, [0,0,0,1,2]
        
        :return:  None
        """
        guess = "spray"
        word = "alloy"
        result = [0, 0, 0, 1, 2]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_heals_hello(self) -> None:
        """
        Test case -  word: heals, guess: hello, [2,2,0,2,0]
        
        :return:  None
        """
        guess = "hello"
        word = "heals"
        result = [2, 2, 0, 2, 0]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_train_tenor(self) -> None:
        """
        Test case -  word: train, guess: tenor, [2,0,1,0,1]
        
        :return:  None
        """
        guess = "tenor"
        word = "train"
        result = [2, 0, 1, 0, 1]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_array_spray(self) -> None:
        """
        Test case -  word: array, guess: spray, [0,0,2,2,2]
        
        :return:  None
        """
        guess = "spray"
        word = "array"
        result = [0, 0, 2, 2, 2]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_melee_erect(self) -> None:
        """
        Test case -  word: melee, guess: erect, [1,0,1,0,0]
        
        :return:  None
        """
        guess = "erect"
        word = "melee"
        result = [1, 0, 1, 0, 0]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))

    def test_word_gauge_range(self) -> None:
        """
        Test case -  word: gauge, guess: range, [0,2,0,2,2]
        
        :return:  None
        """
        guess = "range"
        word = "gauge"
        result = [0, 2, 0, 2, 2]
        self.assertEqual(result, get_letter_scores(word, guess),
                         self.words(word, guess))


if __name__ == '__main__':
    unittest.main()
