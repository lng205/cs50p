from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("8/10") == 80
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(80) == "80%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
