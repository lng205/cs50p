from um import count

def test_count():
    assert count("yammy") == 0
    assert count("hello, um, world") == 1
    assert count("Um, hoo") == 2