from random import *
import sys
sys.path.append('..')
from day7 import *

exampleInput = """
16,1,2,0,4,2,7,1,2,14
""".strip()

exampleData = list(map(parser, exampleInput.split(',')))

def test_part1_example():
    assert part1(exampleData) == 37

def test_part2_example():
    assert part2(exampleData) == 168
