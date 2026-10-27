import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['H'],
    'F': ['H'],
    'G': ['H'],
    'H': []
}

h = {'A': 6, 'B': 4, 'C': 3, 'D': 2,
     'E': 3, 'F': 2, 'G': 1, 'H': 0}

q = [(h['A'], ['A'])]
visited = set()

while q:
    _, path = heapq.heappop(q)
    node = path[-1]

    if node == 'H':
        print("Path:", path)
        break

    if node not in visited:
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                heapq.heappush(q, (h[neighbour], path + [neighbour]))