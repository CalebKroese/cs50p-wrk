import pytest
from fuel import convert, gauge


def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("3/a")   # non-integer
    with pytest.raises(ValueError):
        convert("5/4")   # numerator > denominator
    with pytest.raises(ValueError):
        convert("-1/2")  # negative fraction not allowed
    with pytest.raises(ZeroDivisionError):
        convert("1/0")   # denominator = 0


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"