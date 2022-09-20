# Binary search O(lgN)
def binary_search(arr: list[int], item: int) -> int | None:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        if arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
