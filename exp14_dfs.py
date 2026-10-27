
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

def dfs(node, goal, path):
    if node == goal:
        return path

    for nxt in graph[node]:
        if nxt not in path:
            result = dfs(nxt, goal, path + [nxt])
            if result:
                return result

    return None

print("Path:", dfs('A', 'G', ['A']))
