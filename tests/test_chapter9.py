from src.chapter9 import (longest_common_subsequence, longest_common_substring,
                       optimal_pick)

items = [
{"name":"stereo", "price": 3000, "mass" : 4},
{"name":"laptop", "price": 2000, "mass" : 3},
{"name":"guitar", "price": 1500, "mass" : 1},
]

knapsack_capacity = 4

def test_optimal_pick():
    assert(optimal_pick(items, knapsack_capacity) == [3500, {"guitar", "laptop"}])

def test_longest_common_substring():
    assert(longest_common_substring("defi", "fisd") == "fi")

def test_longest_common_subsequence():
    assert(longest_common_subsequence("fosh", "fish") == 3)
