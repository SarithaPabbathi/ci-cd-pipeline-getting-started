from src.main import add, subtract

def test_add_function():
    assert add(1,2) == 3
    assert add(4, 2) == 6
    assert add(0, 0) == 0


def test_subtract_function():
    assert subtract(1, 2) == -1
    assert subtract(4, 2) == 2
    assert subtract(0, 0) == 0

