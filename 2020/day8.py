import sys

class Machine():
    def __init__(self, lines):
        self.lines = lines[:]
        self.reset()

    def reset(self):
        self.i = 0
        self.step = 1
        self.accum = 0

    def doStep(self):
        self.instruction = self.lines[self.i]
        op = self.instruction[0]
        method = getattr(self, op)
        method()
        self.i += self.step

    def acc(self):
        self.step = 1
        opval = self.instruction[1]
        self.accum += opval

    def nop(self):
        self.step = 1

    def jmp(self):
        opval = self.instruction[1]
        self.step = opval

from aoc import data
def p(x):
    operation, offset = x.split()
    return [operation, int(offset)]

lines = data(parser=p)

def part2(lines):
    m = Machine(lines)
    for trial in range(len(m.lines)):
        if m.lines[trial][0] not in ('jmp', 'nop'):
            continue

        m.reset()

        m.lines[trial][0] = 'jmp' if m.lines[trial][0] == 'nop' else 'nop'

        visited = []
        while m.i not in visited:
            visited.append(m.i)
            try:
                m.doStep()
                if m.i == len(m.lines):
                    print(f"success by changing line {trial} to {m.lines[trial]}")
                    return m.accum
            except IndexError:
                print(f"in the woods: {m.i} is beyond {len(m.lines)}")
                break

        m.lines[trial][0] = 'jmp' if m.lines[trial][0] == 'nop' else 'nop'

print(part2(lines))
