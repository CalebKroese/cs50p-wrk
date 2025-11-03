import pytest
from working import convert


def test_basic_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"


def test_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("09:00 - 17:00")
    with pytest.raises(ValueError):
        convert("9AM5PM")
    with pytest.raises(ValueError):
        convert("hello world")


def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 PM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")