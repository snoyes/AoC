import sys
import copy
data = list(map(list, sys.stdin.read().strip().split('\n')))
content = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
#data = list(map(list, content.strip().split('\n')))

rows = [[0] * (len(data[0]) + 2)]
rows += [[0] + x + [0] for x in data]
rows += [[0] * (len(data[0]) + 2)]

nextdata = copy.deepcopy(rows)
nextdata[1][1] = 'X'

hold = hash(''.join(map(str, rows)))
hnew = hash(''.join(map(str, nextdata)))
while hold != hnew:
    for row in range(len(rows)):
        for col in range(len(rows[row])):
            if rows[row][col] in (0, '.'):
                nextdata[row][col] = rows[row][col]
            else:
                surrounding = rows[row-1][col-1:col+2] + rows[row][col-1:col] + rows[row][col+1:col+2] + rows[row+1][col-1:col+2]
                if rows[row][col] == 'L' and not any(x == '#' for x in surrounding):
                    nextdata[row][col] = '#'
                elif rows[row][col] == '#' and sum(1 for x in surrounding if x == '#') >= 4:
                    nextdata[row][col] = 'L'
                else:
                    nextdata[row][col] = rows[row][col]
    hold = hnew
    hnew = hash(''.join(map(str, nextdata)))
    rows = copy.deepcopy(nextdata)
    #for row in nextdata:
        #print(''.join(map(str, row)))
#
    #print('next')

print(len([x for row in nextdata for x in row if x == '#']))
