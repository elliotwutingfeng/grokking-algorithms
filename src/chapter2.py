# Selection sort O(N**2)
import copy


def selection_sort(arr: list[int]) -> list[int]:
    old_arr = copy.deepcopy(arr)
    new_arr = []
    while old_arr:
        smallest = 0
        for idx, elem in enumerate(old_arr):
            if old_arr[smallest] > elem:
                smallest = idx
        new_arr.append(old_arr.pop(smallest))
    return new_arr
