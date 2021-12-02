from aoc import *
import re

def passport(s):
    return dict(x.split(':') for x in re.findall('\w{3}:[^\s]+', s))

entries = data(parser=passport, delimiter='\n\n')

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def part1(entries):
    return sum([required.issubset(passport.keys()) for passport in entries])

def part2(entries):
    validators = {
            'byr': lambda x: 1920 <= int(x) <= 2002,
            'iyr': lambda x: 2010 <= int(x) <= 2020,
            'eyr': lambda x: 2020 <= int(x) <= 2030,
            'hgt': lambda x: (
                             x.endswith('cm') and 150 <= int(x[:-2]) <= 193 
                             or 
                             x.endswith('in') and 59 <= int(x[:-2]) <= 76
                             ),
            'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
            'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
            'pid': lambda x: re.match('^\d{9}$', x)
            }

    for passport in entries:
        if not required.issubset(passport.keys()) or not all(validators[key](passport[key]) for key in required):
            print(passport, 'bad')
        else:
            print(passport, 'good')

    return sum(
            [
                required.issubset(passport.keys()) and all(validators[key](passport[key]) for key in required) 
                for passport in entries 
            ]
            )

print(len(entries))
exit()
print(part1(entries), part2(entries))

