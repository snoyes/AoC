from aoc import data
import re
from math import prod

content = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
0,4,50
55,2,20
38,6,12
""".strip().split('\n\n')

content = data(delimiter='\n\n')

rules = re.findall(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)', content[0])
rules = {field: [(int(a), int(b)), (int(c), int(d))] for field, a, b, c, d in rules}
myTicket = tuple(map(int, content[1].strip().split('\n')[1].split(',')))
nearbyTickets = content[2].strip().split('\n')[1:]
nearbyTickets = [tuple(map(int, x.split(','))) for x in nearbyTickets]

def invalidSum(ticket, rules):
    allRules = [item for sublist in [rule for rule in rules.values()] for item in sublist] 
    return sum(num for num in ticket if not any(rule[0] <= num <= rule[1] for rule in allRules))

def part1(rules, myTicket, nearbyTickets):
    return sum(invalidSum(ticket, rules) for ticket in nearbyTickets)

def part2(rules, myTicket, nearbyTickets):
    allRules = [item for sublist in [rule for rule in rules.values()] for item in sublist] 
    nearbyTickets = [ticket for ticket in nearbyTickets if all(any(rule[0] <= num <= rule[1] for rule in allRules) for num in ticket)]
    allTickets = nearbyTickets + [myTicket]
    fieldNames = []
    for i in range(len(myTicket)):
        values = [field[i] for field in allTickets]
        fieldNames.append([fieldName for fieldName, fieldRules in rules.items() if all(any(fieldRule[0] <= num <= fieldRule[1] for fieldRule in fieldRules) for num in values)])

    while any(len(choices) > 1 for choices in fieldNames):
        for choice in range(len(fieldNames)):
            if len(fieldNames[choice]) == 1:
                for removal in range(len(fieldNames)):
                    if removal != choice:
                        try:
                            fieldNames[removal].remove(fieldNames[choice][0])
                        except:
                            pass
    fieldNames = [x[0] for x in fieldNames]
    return prod([myTicket[key] for key, name in enumerate(fieldNames) if name.startswith('departure')])


print(part1(rules, myTicket, nearbyTickets))
print(part2(rules, myTicket, nearbyTickets))
