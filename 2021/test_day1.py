import pytest
import random
from day1 import *

minDepth, maxDepth = -10000, 10000
maxNumMeasurements = 1000

exampleInput = """
199
200
208
210
200
207
240
269
260
263
"""

exampleDepth = list(map(int, exampleInput.split()))

def test_part1_example():
    assert part1(exampleDepth) == 7

def test_part1_range():
    numMeasurements = random.randrange(maxNumMeasurements)
    depths = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    assert 0 <= part1(depths) <= max(0, numMeasurements - 1)

def test_part1_decreasing_or_equal():
    numMeasurements = random.randrange(maxNumMeasurements)
    depths = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    depths.sort(reverse=True)
    assert part1(depths) == 0

def test_part1_strictly_increasing():
    numMeasurements = random.randrange(min(maxNumMeasurements, maxDepth - minDepth + 1))
    depths = random.sample(range(minDepth, maxDepth), k=numMeasurements)
    depths.sort()
    assert part1(depths) == max(0, numMeasurements - 1)

def test_part1_delete_value():
    numMeasurements = random.randrange(1, maxNumMeasurements)
    depths = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    i = random.randrange(numMeasurements)
    assert part1(depths) - part1(depths[:i] + depths[i+1:]) in (0, 1)

def test_part1_concatenate_sets():
    numMeasurements = random.randrange(maxNumMeasurements)
    depths1 = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    numMeasurements = random.randrange(maxNumMeasurements)
    depths2 = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    assert part1(depths1 + depths2) - part1(depths1) - part1(depths2) in (0, 1)

def test_part2_example():
    assert part2(exampleDepth) == 5

def test_part2_range():
    numMeasurements = random.randrange(maxNumMeasurements)
    depths = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    assert 0 <= part2(depths) <= max(0, numMeasurements - 3)

def test_part2_decreasing_or_equal():
    numMeasurements = random.randrange(maxNumMeasurements)
    depths = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    depths.sort(reverse=True)
    assert part2(depths) == 0

def test_part2_strictly_increasing():
    numMeasurements = random.randrange(min(maxNumMeasurements, maxDepth - minDepth + 1))
    depths = random.sample(range(minDepth, maxDepth), k=numMeasurements)
    depths.sort()
    assert part2(depths) == max(0, numMeasurements - 3)

def test_part2_delete_value():
    numMeasurements = random.randrange(1, maxNumMeasurements)
    depths = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    i = random.randrange(numMeasurements)
    assert part2(depths) - part2(depths[:i] + depths[i+1:]) in range(-2, 4)

def test_part2_concatenate_sets():
    numMeasurements = random.randrange(maxNumMeasurements)
    depths1 = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    numMeasurements = random.randrange(maxNumMeasurements)
    depths2 = random.choices(range(minDepth, maxDepth), k=numMeasurements)
    assert part2(depths1 + depths2) - part2(depths1) - part2(depths2) in (0, 1, 2, 3)
