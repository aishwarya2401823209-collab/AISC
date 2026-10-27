import heapq

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('D', 3), ('E', 2)],
    'C': [('A', 3), ('F', 2), ('G', 3)],
    'D': [('B', 3), ('H', 3)],
    'E': [('B', 2), ('H', 4)],
    'F': [('C', 2), ('H', 3)],
    'G': [('C', 3), ('H', 2)],
    'H': [('D', 3), ('E', 4), ('F', 3), ('G', 2)]
}

h = {'A': 5, 'B': 4, 'C': 3, 'D': 3,
     'E': 3, 'F': 2, 'G': 1, 'H': 0}

q = [(h['A'], 0, ['A'])]
visited = set()

while q:
    f, cost, path = heapq.heappop(q)
    node = path[-1]

    if node == 'H':
        print("Path:", path)
        print("Total Cost:", cost)
        break

    if node not in visited:
        visited.add(node)

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                new_cost = cost + weight
                heapq.heappush(q, (new_cost + h[neighbour],
                                   new_cost, path + [neighbour]))