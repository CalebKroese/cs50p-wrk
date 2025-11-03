from twttr import shorten


def test_only_vowels():
    assert shorten("AEIOUaeiou") == ""


def test_no_vowels():
    assert shorten("rhythm") == "rhythm"


def test_mixed_case():
    assert shorten("Hello") == "Hll"
    assert shorten("WORLD") == "WRLD"


def test_numbers_and_symbols():
    assert shorten("CS50!") == "CS50!"
    assert shorten("123@OpenAI") == "123@pn"


def test_sentence():
    assert shorten("Twitter is fun!") == "Twttr s fn!"
    