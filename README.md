# grokking algorithms

[![GitHub license](https://img.shields.io/badge/LICENSE-BSD--3--CLAUSE-GREEN?style=for-the-badge)](LICENSE)

Solutions to problems listed in the book "grokking algorithms" by Aditya Y. Bhargava

## Problems

- [x] Binary Search
- [x] Selection Sort
- [x] Recursion
- [x] Maximum Square Plot (Divide & Conquer)
- [x] Quick Sort
- [x] Merge Sort
- [x] Hash Table Implementation
- [x] Breadth First Search
- [x] Dijkstra's Algorithm
- [x] Knapsack problem (Greedy approximation)
- [x] Set-covering Problem
- [x] Traveling Salesperson Problem (Greedy Approximation)
- [x] Knapsack problem (Dynamic Programming Optimal)
- [x] Longest Common Substring
- [x] Longest Common Subsequence

## Requirements

- Python 3.12+

## Setup

```shell
python3 -m venv venv
venv/bin/python3 -m pip install --upgrade pip
venv/bin/python3 -m pip install -r requirements.txt
```

## Formatting

```shell
venv/bin/python3 -m black .
```

## Testing

```shell
venv/bin/python3 -m pytest --cov
```
