# Breadth First Search

from collections import deque

y = "you"
al = "alice"
b = "bob"
c = "claire"
an = "anuj"
p = "peggy"
t = "thom"  # seller
j = "jonny"

graph = {}
graph[y] = [al, b, c]
graph[b] = [an, p]
graph[al] = [p]
graph[c] = [t, j]
graph[an] = []
graph[p] = []
graph[t] = []
graph[j] = []


def person_is_seller(person):
    # Seller's names end with 'm', like 'thom'
    return person[-1] == "m"


def search(name):
    search_queue = deque()
    if name not in graph:
        return False
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print("Searched:", len(searched) + 1)
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False
