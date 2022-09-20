# Knapsack problem (Dynamic Programming Optimal)
def optimal_pick(items, knapsack_capacity) -> list:
    grid = [[[0, set()] for _ in range(knapsack_capacity)] for _ in items]
    for i, item in enumerate(items):
        for j in range(knapsack_capacity):
            previous_max_row = i - 1
            previous_max_value, previous_max_items = (
                (0, set())
                if previous_max_row < 0
                else (grid[previous_max_row][j][0], grid[previous_max_row][j][1])
            )
            remaining_space_column = j - item["mass"]
            current_item_and_remaining_space_value = (
                0
                if item["mass"] - 1 > j
                else (
                    item["price"]
                    + (
                        0
                        if remaining_space_column < 0
                        else grid[previous_max_row][remaining_space_column][0]
                    )
                )
            )
            current_item_and_remaining_space_items = (
                set()
                if item["mass"] - 1 > j
                else (
                    set([item["name"]]).union(
                        set()
                        if remaining_space_column < 0
                        else grid[previous_max_row][remaining_space_column][1]
                    )
                )
            )
            if previous_max_value > current_item_and_remaining_space_value:
                grid[i][j] = [previous_max_value, previous_max_items]
            else:
                grid[i][j] = [
                    current_item_and_remaining_space_value,
                    current_item_and_remaining_space_items,
                ]
    return grid[i][j]


# Longest common substring

# If there are multiple longest common substrings, return the leftmost substring.


def longest_common_substring(a: str, b: str) -> str:
    cell = [
        [0 for _ in range(len(a) + 2)] for _ in range(len(b) + 2)
    ]  # padding of size 1
    longest_substring_coords = (0, 0)
    longest_substring_length = 0  # solution is the largest number in the grid
    for row in range(1, len(b) + 1):
        for column in range(1, len(a) + 1):
            if a[column - 1] != b[row - 1]:
                pass
            else:
                cell[row][column] = cell[row - 1][column - 1] + 1
            if cell[row][column] > longest_substring_length:
                longest_substring_length = cell[row][column]
                longest_substring_coords = row, column
    return b[
        longest_substring_coords[0]
        - longest_substring_length : longest_substring_coords[0]
    ]


# Longest common subsequence

# Returns number of letters in a sequence that 2 words have in common
def longest_common_subsequence(a: str, b: str) -> int:
    cell = [
        [0 for _ in range(len(a) + 2)] for _ in range(len(b) + 2)
    ]  # padding of size 1
    longest_subsequence_length = 0
    for row in range(1, len(b) + 1):
        for column in range(1, len(a) + 1):
            if a[row - 1] != b[column - 1]:
                cell[row][column] = max(cell[row - 1][column], cell[row][column - 1])
            else:
                cell[row][column] = cell[row - 1][column - 1] + 1
            if cell[row][column] > longest_subsequence_length:
                longest_subsequence_length = cell[row][column]
    return longest_subsequence_length
