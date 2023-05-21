# ---------------------------------------------------------------------
# This is the main entry point for the Wordle Scoring
# Information Application.
#
# It is a simple command line application that displays a greeting
# message only.
# ---------------------------------------------------------------------

def information():
    """
    This function displays information about the Wordle Scoring
    code and testing.

    :return: None
    """
    print("This application is NOT a full implementation of Wordle.")
    print()
    print("It contains two parts:")
    print("   1. The wordle game scoring implemented in Python.")
    print("   2. A series of Unit Tests to test the scoring.")
    print()
    print("Folder & File Structure:")
    print("    - Scoring: src/score_words.py")
    print("    - Tests:   tests/test_score_words.py")
    print()
    print("To execute the unit tests use the following command:")
    print("    python -m unittest discover -s tests")
    print()
    print("The unit tests are written using the unittest framework.")
    print()
    print("The source code is available from:")
    print("    https://githug.com/AdyGCode/wordle-scoring")


if __name__ == '__main__':
    information()
