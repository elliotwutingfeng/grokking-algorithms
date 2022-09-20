from itertools import permutations

import pytest
from more_itertools import flatten

from src.chapter4 import (
    max_square_plot_size,
    mergesort,
    quicksort,
    quicksort_hoare,
    quicksort_lomuto,
)


def test_max_square_plot_size():
    assert max_square_plot_size((1680, 640)) == 80
    assert max_square_plot_size((1, 0)) == None
    assert max_square_plot_size((0, 1)) == None


sorting_test_cases = list(
    flatten([[(list(p), sorted(p)) for p in permutations(range(x))] for x in range(3)])
)


@pytest.mark.parametrize("arr, expected", sorting_test_cases)
def test_quicksort(arr: list[int], expected: list[int]):
    assert quicksort(arr) == expected


@pytest.mark.parametrize("arr, expected", sorting_test_cases)
def test_quicksort_lomuto(arr: list[int], expected: list[int]):
    quicksort_lomuto(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", sorting_test_cases)
def test_quicksort_hoare(arr: list[int], expected: list[int]):
    quicksort_hoare(arr)
    assert arr == expected


@pytest.mark.parametrize("arr, expected", sorting_test_cases)
def test_mergesort(arr: list[int], expected: list[int]):
    mergesort(arr)
    assert arr == expected
