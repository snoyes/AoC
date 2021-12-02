from aoc import data
import re

# @ means high-precedence add
# & means low-precedence multiply
class Int:
    def __init__(self, val):
        self._val = val
    def __matmul__(self, other):
        return Int(self._val + other._val)
    def __and__(self, other):
        return Int(self._val * other._val)
    def __mul__(self, other):
        return Int(self._val * other._val)

def calculate(expression, part=1):
    expression = re.sub(r'(\d+)', r'Int(\1)', expression)
    expression = expression.replace('+', '@')
    if part == 2:
        expression = expression.replace('*', '&')
    return eval(expression)._val

contents = data()
print(sum(calculate(expression) for expression in contents))
print(sum(calculate(expression, part=2) for expression in contents))
