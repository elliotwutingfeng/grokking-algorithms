import pytest

from src.chapter1 import binary_search

arr = [1, 3, 5, 7, 9]
test_cases = [
    ([], 1, None),
    ([4], 2, None),
    (arr, 1, 0),
    (arr, 3, 1),
    (arr, 5, 2),
    (arr, 7, 3),
    (arr, 9, 4),
    (arr, 0, None),
    (arr, 2, None),
    (arr, 4, None),
    (arr, 6, None),
    (arr, 8, None),
    (arr, 10, None),
]


@pytest.mark.parametrize("arr, item, expected", test_cases)
def test_binary_search(arr: list[int], item: int, expected: int | None):
    assert binary_search(arr, item) == expected
