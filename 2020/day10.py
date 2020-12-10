# Part 2
from collections import defaultdict
pathcounts = defaultdict(int, {0:1})
jolts = [0] + sorted(map(int, open('input').readlines()))
for j in jolts:
    for reachable in [x for x in range(j+1, j+4) if x in jolts]:
        pathcounts[reachable] += pathcounts[j]
print(pathcounts[max(jolts)])
