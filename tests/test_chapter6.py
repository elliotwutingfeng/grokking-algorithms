from src.chapter6 import search


def test_search():
    assert search("you") == True  # Has connection to seller
    assert search("claire") == True  # Has connection to seller
    assert search("alice") == False  # No connection to seller
    assert search("jonny") == False  # No connection to seller
    assert search("peggy") == False  # No connection to seller
    assert search("bob") == False  # No connection to seller
    assert search("claires") == False  # Name not in graph
