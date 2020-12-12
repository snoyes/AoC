def data(parser=str, delimiter='\n'):
    import sys
    lines = sys.stdin.read().strip().split(delimiter)
    return [parser(line) for line in lines]

def first(iterable, default=None):
    return next(iter(iterable), None)
