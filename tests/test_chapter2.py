import pytest

from src.chapter2 import selection_sort

arr = [9, 1, 3, 7, 5]
test_cases = [
    ([], []),
    ([1], [1]),
    (arr, [1, 3, 5, 7, 9]),
]


@pytest.mark.parametrize("arr, expected", test_cases)
def test_selection_sort(arr: list[int], expected: list[int]):
    assert selection_sort(arr) == expected
