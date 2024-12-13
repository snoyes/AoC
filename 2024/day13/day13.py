import sympy as sp
import re

def do_calc(machines, extra=0):
    pressA, pressB = sp.symbols('pressA pressB', integer=True)
    return sum(
        3*solution[pressA] + solution[pressB]
        for (ax, ay, bx, by, px, py) in machines
        if  (eq1 := ax*pressA + bx*pressB - px - extra)
        and (eq2 := ay*pressA + by*pressB - py - extra)
        and (solution := sp.solve((eq1, eq2), (pressA, pressB)))
    )

machines = [list(map(int, re.findall(r'\d+', line))) for line in open(0).read().strip().split('\n\n')]
print(do_calc(machines))
print(do_calc(machines, extra=10000000000000))
