from aoc import data
from functools import cache
import regex
contents = data(delimiter='\n\n')
contents[0] = contents[0].replace('"', '')
rules = regex.findall(r"(\d+): ([^\n]*)\n*", contents[0])
rules = {int(key): [x.strip().split() for x in val.strip().split('|')] for key, val in rules}
strings = contents[1].split('\n')

def getReg(key):
    elements = []
    for lineIndex, line in enumerate(rules[key]):
        elements.append([])
        for valIndex, val in enumerate(line):
            if val.isdigit():
                elements[lineIndex].append(getReg(int(val)))
            else:
                return val
    return '(' + '|'.join(''.join(v) for v in elements) + ')'

def part1(rules, contents):
    reg = '^' + getReg(0) + '$'
    print(len([x for x in strings if regex.match(reg, x)]))

@cache
def getReg2(key):
    if key == 11:
        k42 = getReg2(42)
        k31 = getReg2(31)
        #k11 = f"(({k42}{k31})|({k42}\\2{k31}))"
        k11 = f"(?P<foo>({k42}{k31})|({k42}(?&foo){k31}))"
        print(f'returning {k11} for {key}')
        return k11

    if key == 8:
        k42 = getReg2(42)
        k8 = f"(({k42})+)"
        print(f'returning {k8} for {key}')
        return k8

    elements = []
    for lineIndex, line in enumerate(rules[key]):
        elements.append([])
        for valIndex, val in enumerate(line):
            if val.isdigit():
                elements[lineIndex].append(getReg2(int(val)))
            else:
                print(f'returning val {val} for {key}')
                return val

    k = '(' + ')|('.join(''.join(v) for v in elements) + ')'
    #if len(elements) > 1:
    k = '(' + k + ')'
    print(f'finally returning {k} for {key}')
    return k


def part2(rules, contents):
    reg = getReg2(0)
    #reg = getReg2(11)

    print('\n'.join([x for x in strings if regex.fullmatch(reg, x)]))
    print(len([x for x in strings if regex.fullmatch(reg, x)]))

#part1(rules, contents)
part2(rules, contents)

