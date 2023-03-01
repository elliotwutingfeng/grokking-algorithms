"""
Core features

- Create an empty hash table
- Insert a key-value pair to the hash table
- Delete a key-value pair from the hash table
- Find a value by key in the hash table
- Update the value associated with an existing key
- Check if the hash table has a given key

Non-essential features

- Create a hash table from a Python dictionary
- Create a shallow copy of an existing hash table
- Return a default value if the corresponding key is not found
- Report the number of key-value pairs stored in the hash table
- Return the keys, values, and key-value pairs
- Make the hash table iterable
- Make the hash table comparable by using the equality test operator
- Show a textual representation of the hash table

Corner cases

- Resolve hash code collisions
- Retain insertion order
- Resize the hash table dynamically
- Calculate the load factor

"""

from collections import deque
from typing import Any, NamedTuple


class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    def __init__(self, capacity=8, load_factor_threshold=0.6):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("Load factor must be a number between (0, 1]")
        self._buckets = [deque() for _ in range(capacity)]
        self._keys = [] # to remember insertion order
        self._load_factor_threshold = load_factor_threshold

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary))
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __len__(self):
        return len(self.pairs)

    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._buckets = copy._buckets

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        return True

    def __delitem__(self, key):
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[index]
                self._keys.remove(key)
                break
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                bucket[index] = Pair(key, value)
                break
        else:
            bucket.append(Pair(key, value))
            self._keys.append(key)

    def __getitem__(self, key):
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def __iter__(self):
        yield from self.keys

    def __str__(self):
        # Notice the !r conversion flag in the template string, which enforces calling repr()
        # instead of the default str() on keys and values.
        # This ensures more explicit representation, which varies between data types.
        # For example, it wraps strings in single apostrophes.
        pairs = [f"{key!r}: {value!r}" for key, value in self.pairs]
        return "{" + ", ".join(pairs) + "}"

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)

    @property
    def keys(self):
        return self._keys.copy()

    @property
    def values(self):
        return [self[key] for key in self.keys]

    @property
    def pairs(self):
        return [(key, self[key]) for key in self.keys]

    @property
    def capacity(self):
        return len(self._buckets)

    @property
    def load_factor(self):
        return len(self) / self.capacity

    def _index(self, key):
        return hash(key) % self.capacity

# In the beginning, bob hashes to key1
# employees = {alice: "project manager", bob: "engineer"} -> employees contains key1
# bob.name = "Bobby" -> bob now hashes to key2 but employees still contains key1 only.
# employees[bob] now gives error because you are looking for key2 in employees, which contains key1 only.
# employees[Person("Bobby")] also gives error because you are looking for key2 in employees, which contains key1 only.
# employees[Person("Bob")] looks for key1 into employees, and employees contains key1. But it still fails
# because the equality check for name attribute fails ("Bob" != "Bobby").
# Since hash codes are typically derived from an object’s attributes, their state
# should be fixed and never change over time. In practice, this also means that objects intended as
# hash table keys should be immutable themselves.
