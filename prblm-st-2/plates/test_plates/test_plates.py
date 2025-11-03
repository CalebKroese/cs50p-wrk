from plates import is_valid


def test_length():
    assert is_valid("A") == False  # too short
    assert is_valid("ABCDEFG") == False  # too long
    assert is_valid("AB") == True  # valid min
    assert is_valid("ABC123") == True  # valid max


def test_start_with_letters():
    assert is_valid("AB123") == True
    assert is_valid("A1234") == False  # only one starting letter
    assert is_valid("12AB") == False  # starts with digits


def test_numbers_rules():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False  # first number zero not allowed
    assert is_valid("CS50P") == False  # letters after numbers not allowed


def test_punctuation_and_symbols():
    assert is_valid("PI3.14") == False  # contains period
    assert is_valid("CS 50") == False  # contains space
    assert is_valid("CS@50") == False  # contains special char
    assert is_valid("HELLO") == True   # all letters valid


def test_case_sensitivity():
    # Case doesn’t matter since all alphanumeric are valid
    assert is_valid("cs50") == True
    assert is_valid("Cs50") == True