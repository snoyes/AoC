from random import *
from day9 import *

exampleInput = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip()

exampleData = list(map(parser, exampleInput.split('\n')))

def test_part1_example():
    assert part1(exampleData) == 15

def test_part2_example():
    assert part2(exampleData) == 1134
