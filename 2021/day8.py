from aoc import data

def part1(inputData):
    return sum(sum(len(x) in (2, 3, 4, 7) for x in line['digits']) for line in inputData)

def getSignalToDigit(line):
    digitToSignal = dict()
    for signal in sorted(map(set, line['signals']), key=len): # sorting by length ensures '1' and '4' are solved early
        match len(signal):
            case 2: digit = '1'
            case 3: digit = '7'
            case 4: digit = '4'
            case 5 | 6:
                match (len(signal), len(signal - digitToSignal['1']), len(signal - digitToSignal['4'])):
                    case (5, 4, 3): digit = '2'
                    case (5, 3, 2): digit = '3'
                    case (5, 4, 2): digit = '5'
                    case (6, 4, 3): digit = '0'
                    case (6, 5, 3): digit = '6'
                    case (6, 4, 2): digit = '9'
            case 7: digit = '8'
        digitToSignal[digit] = signal
    return {''.join(sorted(v)): k for k, v in digitToSignal.items()}

def part2(inputData):
    total = 0
    for line in inputData:
        signalToDigit = getSignalToDigit(line)
        total += int(''.join(signalToDigit[''.join(sorted(d))] for d in line['digits']))
    return total

def parser(line):
    signal, digits = line.split(' | ')
    return {'signals': signal.split(), 'digits': digits.split()}

if __name__ == "__main__":
    inputData = data(parser=parser)
    print(part1(inputData))
    print(part2(inputData))
