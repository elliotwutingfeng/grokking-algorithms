# Hash tables
# The chapter on hash tables in this book could have gone deeper on implementing hash tables from scratch (for learning purposes)
# A good reference is https://realpython.com/python-hash-table

# equivalent hashes
hash(2**61) == hash(1)

# Python uses hash randomization to deter Denial of Service attacks from
# abusing hash collisions
hash(
    "Lorem"
)  # running this again in another python invocation gives a different result

# Hash randomization can be disabled by setting environment variable
# PYTHONHASHSEED to a fixed value (e.g. set PYTHONHASHSEED=1)

# Mutable types cannot be hashed (e.g. lists, dicts, sets)

# hash() produces a fixed-size output; hence it projects a potentially infinite set of values onto a finite space.
# By the pigeonhole principle, there will be hash collisions.

# hash_distribution.

from collections import Counter


def distribute(items, num_containers, hash_function=hash):
    c = Counter()
    for item in items:
        c.update({hash_function(item) % num_containers: 1})
    return c


def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")
    print()


from string import printable

# printable is
# '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'

# hash() distribution is roughly uniform, but not perfect.
print("2 buckets")
plot(distribute(printable, num_containers=2))
print("15 buckets")
plot(distribute(printable, num_containers=15))


# ord hash function
def hash_function(text):
    return sum(ord(character) for character in text)


# Not only is it string-specific, but it also suffers from poor distribution of hash codes,
# which tend to form clusters at similar input values.

# We can try to support non-string types and distinguish between similar values of different types
# like "3.14" vs 3.14, by using repr()


# ord hash function with repr()
def hash_function_repr(text):
    return sum(ord(character) for character in repr(text))


# To tackle the issue with anagrams, like Loren and Loner, we can include character position in addtion to value
def hash_function_position_value(text):
    # start from 1 otherwise first value is discarded
    return sum(
        index * ord(character) for index, character in enumerate(repr(text), start=1)
    )


# Now we have low collisions, but long strings slow down the hash function a lot.
print("Working on slow hash function...")
hash_function_position_value("This is very long and slow!" * 1_000_000)
print("DONE!")

print("Distribution is also not uniform")
plot(distribute(printable, 6, hash_function_position_value))


# Moreover, there are six containers available, but one is missing from the histogram. This problem
# stems from the fact that the two apostrophes added by repr() cause virtually all keys
# in this example to result in an even hash number.
# We can fix this by removing left apostrophe if it exists
def hash_function_allow_odd_hash_number(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), 1)
    )


# Looks better now
plot(distribute(printable, 6, hash_function_allow_odd_hash_number))

import sys

print(
    sys.hash_info.algorithm
)  # Python currently uses SipHash for strings and byte sequences
