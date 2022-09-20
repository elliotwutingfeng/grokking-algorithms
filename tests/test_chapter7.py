from src.chapter7 import find_shortest_path


def test_find_shortest_path():
    graph: dict = {
        "start": {"a": 6, "b": 2, "c": 3},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "c": {"a": 1},
        "fin": {},
    }
    path, total_cost = find_shortest_path(graph, "start", "fin")
    assert path == ["start", "c", "a", "fin"]
    assert total_cost == 5

    path, total_cost = find_shortest_path(graph, "start", "noexist")
    assert path == []
    assert total_cost == -1
