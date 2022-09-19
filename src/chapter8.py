import math


# Knapsack problem (Greedy Approximation)
def greedy_pick(items: list[dict[str,str|int]], knapsack_capacity: int) -> int:
    total_value: int = 0
    for item in sorted(items,key=lambda x : x["price"], reverse=True):
        mass = item["mass"]
        if type(mass) is int and mass > knapsack_capacity:
            continue
        price = item["price"]
        total_value += price  # type: ignore
        knapsack_capacity -= mass  # type: ignore
    return total_value

def greedy_pick_price_per_mass(items: list[dict[str,str|int]], knapsack_capacity: int) -> int:
    total_value: int = 0
    for item in sorted(items,key=lambda x : x["price"]/x["mass"], reverse=True):  # type: ignore
        mass = item["mass"]
        if type(mass) is int and mass > knapsack_capacity:
            continue
        price = item["price"]
        total_value += price  # type: ignore
        knapsack_capacity -= mass  # type: ignore
    return total_value

# Set-covering problem
def set_covering(stations, states_to_cover) -> set[str]:
    final_stations = set()

    while states_to_cover:
        # Get station which covers the most stations that are not yet covered
        stations_and_new_states_covered_by_station: list[tuple[str,set[str]]] = sorted(
            ((station, states_to_cover.intersection(states_for_station)) for station, states_for_station in stations.items()),
             key=lambda x: len(x[1])
        )
        best_station, states_covered_by_best_station = stations_and_new_states_covered_by_station[-1]
        final_stations.add(best_station)
        states_to_cover -= states_covered_by_best_station

    return final_stations

# Traveling Salesperson Problem (Greedy Approximation)

# Given a starting node (denoted by x-y spatial coordinates), find the nearest node that
# has not been visited yet, move to that node, add distance travelled to total distance, then find the nearest node... until all nodes
# have been visited.

# Repeat the above process for all possible starting nodes, then choose the path with the lowest total distance.

# Time Complexity : O(N**3)

# Alternatively, the networkx library offers the traveling_salesman_problem() function

def travelling_salesperson(nodes) -> tuple[list[int|None], float]:
    best_path_and_total_distance: tuple[list[int|None], float] = ([], float("inf"))

    for first_node_idx in range(len(nodes)):
        current_node_idx: int = first_node_idx
        nodes_to_visit = set(range(len(nodes))) - set((current_node_idx,))
        path: list[int | None] = [current_node_idx]
        total_distance = 0.0
        while nodes_to_visit:
            closest_distance = float("inf")
            closest_node_idx = None
            for idx in nodes_to_visit:
                distance = math.dist(nodes[current_node_idx], nodes[idx])
                if distance < closest_distance:
                    closest_distance = distance
                    closest_node_idx = idx
            path.append(closest_node_idx)
            total_distance += closest_distance
            # print("Node %s -> Node %s Distance : %d" % (current_node_idx, closest_node_idx, closest_distance))
            nodes_to_visit -= set((closest_node_idx,))
            current_node_idx = closest_node_idx  # type: ignore
        # print("Path:", path, "Total Distance:", total_distance)
        if total_distance < best_path_and_total_distance[1]:
            best_path_and_total_distance = path, total_distance
    return best_path_and_total_distance
