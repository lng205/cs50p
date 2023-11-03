from twttr import shorten

def test_lower():
    assert shorten("hello, 123") == "hll, 123"

def test_higher():
    assert shorten("HELLO") == "HLL"
