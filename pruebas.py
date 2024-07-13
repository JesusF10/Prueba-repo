import sys
import pytest
from calculator import square


def test_square_1():
    assert square(3) == 9
    assert square(0) == 0
    assert square(-3) == 9
    assert square(1) == 1
    assert square(2) == 4
    assert square(-5) == 25

def test_square_2():
    assert square(3) == 9
    assert square(1) == 1
    assert square(-3) == 9
    assert square(1) == 1
    


