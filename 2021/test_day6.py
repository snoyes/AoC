from random import *
import sys
sys.path.append('..')
from day6 import *

exampleInput = "3,4,3,1,2"
exampleData = list(map(parser, exampleInput.split(',')))

def test_part1_example():
    assert part1(exampleData) == 5934

def test_part2_example():
    assert part2(exampleData) == 26984457539 
