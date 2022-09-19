# (Maximum Square Plot) Divide & conquer

def max_square_plot_size(dimensions: tuple[int,int]) -> int | None:
    def aux(shorter: int, longer: int) -> int:
        leftover = longer % shorter
        return aux(leftover,shorter) if leftover else shorter
    return None if not dimensions[0] or not dimensions[1] else aux(min(dimensions),max(dimensions))


# Quick sort O(NlgN) average
# When array is already sorted, and min/max element is always chosen as pivot, performance degrades to O(N**2)

from secrets import choice


def quicksort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = choice(range(len(arr)))
    pivot_val = arr[pivot]
    smaller, larger = [], []
    for idx,elem in enumerate(arr):
        if idx == pivot:
            continue
        if elem <= pivot_val:
            smaller.append(elem)
        else:
            larger.append(elem)
    return quicksort(smaller) + [pivot_val] + quicksort(larger)

# Quick sort In-Place Lomuto partitioning

def lomuto_partitioning(arr: list[int], low: int, high: int) -> int:
    # Set rightmost element as pivot
    pivot = arr[high]
    i = low - 1 # i+1 denotes pivot insertion point, initially, pivot is to be inserted at index 0
    for j in range(low, high):
        # from left to right, check if element <= pivot
        if arr[j] <= pivot:
            # if it is, increment pivot insertion point, and swap it with element just before pivot insertion point
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    # finally, swap pivot with element at pivot insertion point
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return i + 1

def quicksort_lomuto(arr: list[int], low: int = None, high: int = None) -> None:
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = lomuto_partitioning(arr, low, high)
        quicksort_lomuto(arr, low, pivot_idx-1)
        quicksort_lomuto(arr, pivot_idx+1, high)


# Quick sort In-Place Hoare's partitioning

def hoare_partitioning(arr: list[int], low: int, high: int) -> int:
    # Set leftmost element as pivot
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[j], arr[i] = arr[i], arr[j]

def quicksort_hoare(arr: list[int], low: int = None, high: int = None) -> None:
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = hoare_partitioning(arr, low, high)
        quicksort_hoare(arr, low, pivot_idx)
        quicksort_hoare(arr, pivot_idx+1, high)

# Merge sort O(NlgN) average

# Merge sort often accesses data sequentially while Quick sort often accesses data randomly.
# So it is more suitable for sorting Linked Lists than Quick sort.
# No matter how the array is arranged, merge sort will go through the entire process, giving it a best-case of O(NlgN)

def mergesort(arr: list[int]) -> None:
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    mergesort(L)
    mergesort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
