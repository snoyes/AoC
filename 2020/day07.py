import re
with open('input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

for line in lines: 
    outerBag = re.findall(r'^\w+ \w+', line)[0]
    innerBags = re.findall(r'(\d) (\w+ \w+)', line)
    for innerBag in innerBags:
        print(f"{outerBag}\t{innerBag[0]}\t{innerBag[1]}")
