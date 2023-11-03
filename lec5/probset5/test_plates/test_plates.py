from plates import is_valid

def test_start_letters():
    assert is_valid("1F") == False
    assert is_valid("F1") == False
    assert is_valid("FA") == True

def test_length():
    assert is_valid("FF111111") == False
    assert is_valid("FF11") == True

def test_digit():
    assert is_valid("FF0A0") == False
    assert is_valid("FFA00") == False
    assert is_valid("FFA10") == True
    assert is_valid("FF21A") == False

def test_character():
    assert is_valid("FF,") == False
    assert is_valid("FF.") == False
    assert is_valid("FF ") == False
