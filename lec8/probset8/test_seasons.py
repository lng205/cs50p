import pytest
from seasons import get_birth

def test_get_birth():
    with pytest.raises(ValueError):
        get_birth("hiihooo")
    with pytest.raises(ValueError):
        get_birth("20000101")
    with pytest.raises(ValueError):
        get_birth("January 1, 1999")
