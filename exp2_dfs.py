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
stack = [[start]]
visited = set()

while stack:
    path = stack.pop()
    node = path[-1]

    if node == goal:
        print("Path:", path)
        break

    if node not in visited:
        visited.add(node)

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(path + [neighbour])
else:
    print("Path not found")