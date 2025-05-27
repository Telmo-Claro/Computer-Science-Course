from math_func import *

def test_add_numbers():
    assert add_numbers(2,3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0