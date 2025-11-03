from seasons import minutes_lived
from datetime import date

def test_minutes_lived_one_year():
    d1 = date(2000, 1, 1)
    d2 = date(2001, 1, 1)
    assert minutes_lived(d1, d2) == 525600

def test_minutes_lived_leap_year():
    d1 = date(2019, 1, 1)
    d2 = date(2020, 1, 1)
    assert minutes_lived(d1, d2) == 525600  # still normal year
    d3 = date(2020, 1, 1)
    d4 = date(2021, 1, 1)
    assert minutes_lived(d3, d4) == 527040  # leap year adds one day

def test_minutes_lived_future_birth():
    d1 = date(2100, 1, 1)
    d2 = date(2025, 1, 1)
    assert minutes_lived(d1, d2) == 0