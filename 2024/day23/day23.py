import networkx as nx
from itertools import combinations
G = nx.Graph()
G.add_edges_from(line.split('-') for line in open(0).read().strip().split())
print(len(set(tuple(sorted(combo)) for clique in nx.find_cliques(G) for combo in combinations(clique, r=3) if any(node.startswith('t') for node in combo))))
print(','.join(sorted(sorted(nx.find_cliques(G), key=len)[-1])))
