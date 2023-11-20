import pytest
from working import convert

def test_convert():
    assert convert("5:00 AM to 5:00 PM") == "05:00 to 17:00"
    assert convert("5 PM to 8 AM") == "17:00 to 08:00"
    with pytest.raises(ValueError):
        convert("7:60 AM to 4:30 PM")
    with pytest.raises(ValueError):
        convert("7:60 AM - 4:30 PM")