from aoc import data
import re

lines = data()

for line in lines: 
    outerBag = re.findall(r'^\w+ \w+', line)[0]
    innerBags = re.findall(r'(\d) (\w+ \w+)', line)
    for innerBag in innerBags:
        print(f"{outerBag}\t{innerBag[0]}\t{innerBag[1]}")
