import pytest
import main

def test_add_zero():
    assert main.add(0, 5) == 5

def test_add_commute():
    assert main.add(3, 5) == main.add(5, 3)

@pytest.mark.parametrize("x,y,expected", [(3, 5, 8), (-1, 1, 0), (10, 11, 21)])
def test_add_foo(x, y, expected):
    assert main.add(x, y) == expected 

def test_add_none():
    with pytest.raises(Exception):
        main.add(None, 3)