import numpy as np
import igraph as ig
from collections import defaultdict, deque


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited


def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.appendleft((next, path+[next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


# TASK 1
n = 100
m = 200
g = ig.Graph.Erdos_Renyi(n=n, m=m)
adj_matrix = g.get_adjacency()
adj_list = defaultdict(list)
for i in range(len(g.vs)):
    g.vs[i]["id"] = i
    g.vs[i]["label"] = str(i)

for i in range(100):
    adj_list[i] = []


for i in range(n):
    for j in range(n):
        if adj_matrix[i][j]:
            adj_list[i].append(j)


adj_list = dict(adj_list)

print("Adj matrix 2nd row: ", adj_matrix[2])
print("Adj matrix 5th row: ", adj_matrix[5])
print("Adj matrix 10th row: ", adj_matrix[10])
print("Adj list: ", adj_list)


visual_style = {"vertex_label_size": 14}
ig.plot(g, target='graph.png', **visual_style)

# TASK 2.1
all_components = []
visited = [False for i in range(n+1)]


def dfs(graph, node, comp):
    # marking node as visited.
    visited[node] = True

    # appending node in the component list
    comp.append(node)
    # visiting neighbours of the current node
    for neighbour in graph[node]:
        # if the node is not visited then we call dfs on that node.
        if not visited[neighbour]:
            dfs(graph, neighbour, comp)


for i in range(n):
    if not visited[i]:
        component = []
        dfs(adj_list, i, component)
        all_components.append(component)


print("Components: ", all_components)
print("Number of components: ", len(all_components))


# TASK 2.2
rand1 = np.random.randint(1, 100)
rand2 = np.random.randint(1, 100)
if rand1 == rand2:
    rand2 = np.random.randint(1, 100)

print("Shortest path from ", rand1, "to ", rand2, ": ", shortest_path(adj_list, rand1, rand2))

