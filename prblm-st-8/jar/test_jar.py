import pytest
from jar import Jar


def test_init_default():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_init_custom_capacity():
    jar = Jar(20)
    assert jar.capacity == 20
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("ten")


def test_deposit_and_str():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(1)  # exceeds capacity


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    assert str(jar) == "🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(3)  # not enough cookies


def test_size_and_capacity_properties():
    jar = Jar(8)
    jar.deposit(5)
    assert jar.size == 5
    assert jar.capacity == 8