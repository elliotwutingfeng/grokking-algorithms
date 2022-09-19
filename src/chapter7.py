# Dijkstra's Algorithm

def find_shortest_path(graph, source, destination) -> tuple[list, float]:
    def get_keys(dictionary) -> set[str]:
        """
        Get all keys in nested dict
        """
        result = set()
        for key, value in dictionary.items():
            if type(value) is dict:
                new_keys = get_keys(value)
                result.add(key)
                result.update(new_keys)
            else:
                result.add(key)
        return result
    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in (node for node in costs if node not in processed):
            cost = costs[node]
            if cost < lowest_cost:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    all_nodes = get_keys(graph)
    if source not in all_nodes or destination not in all_nodes:
        return ([], -1)
    costs = {**{node : float("inf") for node in all_nodes}, **graph[source]}
    parents = {**{destination : None for _ in all_nodes}, **{k:source for k in graph[source]}}

    processed = set()
    while (node := find_lowest_cost_node(costs)) is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)

    node = destination
    path = [node]
    while node in parents:
        node = parents[node]
        path.insert(0, node)
    return path, costs[destination]
