rules, pages = open(0).read().strip().split('\n\n')
rules = {tuple(map(int, x.split('|'))) for x in rules.split()}
pages = [ list(map(int, x.split(','))) for x in pages.split()]

from functools import cmp_to_key
key = cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))

print( sum(new_row[len(row)//2] for row in pages if row == (new_row := sorted(row, key=key))) )
print( sum(new_row[len(row)//2] for row in pages if row != (new_row := sorted(row, key=key))) )
