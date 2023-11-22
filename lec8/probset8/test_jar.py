import pytest
from jar import Jar

def test_init():
    assert Jar().capacity == 12
    assert Jar(22).capacity == 22
    with pytest.raises(ValueError):
        Jar(-5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(22)
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar(22)
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(10)
