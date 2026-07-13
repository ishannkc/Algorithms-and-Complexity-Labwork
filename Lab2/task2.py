#Probabilistic Algorithm

#Karger's Minimum Cut Algorithm
import random

def build_graph(edges):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    return graph


def karger_min_cut(graph):
    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        # merge v into u
        graph[u].extend(graph[v])
        for neighbor in graph[v]:
            graph[neighbor] = [u if x == v else x for x in graph[neighbor]]

        # remove self loops
        graph[u] = [x for x in graph[u] if x != u]

        del graph[v]

    return len(list(graph.values())[0])


# Main Program
num_edges = int(input("Enter number of edges: "))

print("Enter each edge as two vertex numbers separated by a space.")
print("Example: 1 2")

edges = []
for i in range(num_edges):
    u, v = map(int, input(f"Edge {i + 1}: ").split())
    edges.append((u, v))

trials = int(input("Enter number of trials to run: "))

print("\nGraph edges entered:", edges)

min_cut = float('inf')
for t in range(trials):
    graph = build_graph(edges)
    cut = karger_min_cut(graph)
    print(f"Trial {t + 1}: cut size = {cut}")
    if cut < min_cut:
        min_cut = cut

print("\nMinimum cut found after", trials, "trials:", min_cut)