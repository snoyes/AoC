import networkx
import math
from random import sample
from collections import Counter
from aocd import data

G = networkx.Graph()
for line in data.split('\n'):
    left, others = line.split(': ')
    G.add_edges_from((left, other) for other in others.split(' '))

# Half the possible paths have to cross one of the bridges
# So pick a bunch of random pairs of nodes, find which edges are most common
edges = Counter()
for _ in range(1000):
    n1, n2 = sample(list(G.nodes()), k=2)
    path = networkx.shortest_path(G, n1, n2)
    edges.update([tuple(sorted(x)) for x in zip(path, path[1:])])
cuts = [path for path, _ in edges.most_common(3)]
G.remove_edges_from(cuts)
a = math.prod(len(c) for c in networkx.connected_components(G))
print(a)