
def earliest_ancestor(ancestors, starting_node):
    vertices = {}
    for i in ancestors:
        parent = i[0]
        child = i[1]
        if child not in vertices:
            vertices[child] = set()
            vertices[child].add(parent)
        elif vertices[child]:
            vertices[child].add(parent)
    
    Q = [starting_node]
    visited = []
    parents = []
    while Q:
        current = Q.pop()
        visited.append(current)
        if current in vertices:
            parents = []
            for i in vertices[current]:
                if i not in visited:
                    Q.append(i)
                    parents.append(i)
    if len(parents) == 0:
        return -1
    elif len(parents) == 1:
        return parents[0]
    elif len(parents) == 2:
        if parents[0] < parents[1]:
            return parents[0]
        else:
            return parents[1]