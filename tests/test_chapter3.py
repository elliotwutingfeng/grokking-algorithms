import math

import pytest

from src.chapter3 import factorial

test_cases = [(x, math.factorial(x)) for x in range(10)]


@pytest.mark.parametrize("int, expected", test_cases)
def test_factorial(int: int, expected: int):
    assert factorial(int) == expected
