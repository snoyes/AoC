def is_solvable(total, nums, concat=False):
    frontier = [(nums[0], 1)]
    while frontier:
        node, i = frontier.pop()
        nextnode = nums[i]

        neighbors = [node + nextnode, node * nextnode]
        if concat:
            neighbors.append(int(str(node) + str(nextnode)))

        if total in neighbors and i == len(nums) - 1:
            return True
        elif i < len(nums) - 1:
            frontier.extend([(neighbor, i+1) for neighbor in neighbors if neighbor <= total])

    return False

part1 = part2 = 0
for line in open(0):
    total, *nums = map(int, line.replace(':', '').split())
    if is_solvable(total, nums):
        part1 += total
        part2 += total
    else:
        part2 += is_solvable(total, nums, True) * total

print(part1)
print(part2)
