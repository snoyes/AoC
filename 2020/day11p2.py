from aoc import data
import copy
#data = list(map(list, sys.stdin.read().strip().split('\n')))
def p(line):
    return list(line)
contents = data(parser=p)

rows = [[0] * (len(contents[0]) + 2)]
rows += [[0] + x + [0] for x in contents]
rows += [[0] * (len(contents[0]) + 2)]

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
                surrounding = []

                #up
                x = -1
                y = 0
                while rows[row+x][col+y] == '.':
                    x -= 1
                surrounding.append(rows[row+x][col+y])

                #up right
                x = -1
                y = 1
                while rows[row+x][col+y] == '.':
                    x -= 1
                    y += 1
                surrounding.append(rows[row+x][col+y])

                #right
                x = 0 
                y = 1
                while rows[row+x][col+y] == '.':
                    y += 1
                surrounding.append(rows[row+x][col+y])

                #down right
                x = 1
                y = 1
                while rows[row+x][col+y] == '.':
                    x += 1
                    y += 1
                surrounding.append(rows[row+x][col+y])

                #down
                x = 1
                y = 0
                while rows[row+x][col+y] == '.':
                    x += 1
                surrounding.append(rows[row+x][col+y])

                #down left
                x = 1
                y = -1
                while rows[row+x][col+y] == '.':
                    x += 1
                    y -= 1
                surrounding.append(rows[row+x][col+y])

                #left
                x = 0 
                y = -1
                while rows[row+x][col+y] == '.':
                    y -= 1
                surrounding.append(rows[row+x][col+y])

                #up left
                x = -1
                y = -1
                while rows[row+x][col+y] == '.':
                    x -= 1
                    y -= 1
                surrounding.append(rows[row+x][col+y])

                if rows[row][col] == 'L' and not any(x == '#' for x in surrounding):
                    nextdata[row][col] = '#'
                elif rows[row][col] == '#' and sum(1 for x in surrounding if x == '#') >= 5:
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
