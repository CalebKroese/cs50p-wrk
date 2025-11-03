from um import count


def test_basic_usage():
    assert count("hello, um, world") == 1
    assert count("um um um") == 3


def test_case_insensitive():
    assert count("Um, excuse me") == 1
    assert count("Um, Um, um") == 3


def test_not_substings():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0


def test_with_punctuation():
    assert count("um?") == 1
    assert count("...um...") == 1
    assert count("Um!") == 1


def test_empty_and_no_um():
    assert count("") == 0
    assert count("hello world") == 0