def cycleInGraph(edges):
    # Write your code here.
    for i in range(len(edges)):
        if dfs(edges, i):
            return True
    return False
    
def dfs(edges, target):
    stack = [target]
    visited = set()
    while stack:
        curr = stack.pop()
        if target in edges[curr]:
            return True
        visited.add(curr)
        for vertex in edges[curr]:
            if vertex not in visited:
                stack.append(vertex)
    return False

