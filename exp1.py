from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start = 'A'
goal = 'G'
q = deque([[start]])
visited = {start}

while q:
    path = q.popleft()
    node = path[-1]

    if node == goal:
        print("Path:", path)
        break

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.add(neighbour)
            q.append(path + [neighbour])