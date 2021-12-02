from random import *
from day3 import *

exampleInput = """

""".strip()

exampleData = list(map(parser, exampleInput.split("\n")))

def test_part1_example():
    assert part1(exampleData) == None
