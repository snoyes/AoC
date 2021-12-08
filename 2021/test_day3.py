from random import *
from day3 import *

exampleInput = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()

exampleData = exampleInput.split("\n")

def test_part1_example():
    assert part1(exampleData) == 198

def test_part2_example():
    assert part2(exampleData) == 230
