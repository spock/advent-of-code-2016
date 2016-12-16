# day 7 puzzle 1
# Let's write an almost-elegant buffered look-back stream processor for this...
from collections import deque

def is_abba(s):
    """Check if 4 given characters (in a list) form an ABBA."""
    return True if s[0] != s[1] and s[0] == s[3] and s[1] == s[2] else False

inside_square = False
this_has_abba = False
total_abba = 0
with open('day_7_puzzle_1.txt') as fh:
    for line in fh:
        buffer = deque(maxlen = 4)
        line = line.strip()
        # print(line)
        this_has_abba = False
        for char in line:
            if '[' == char:
                # print('\tentering square brackets')
                inside_square = True
                buffer = deque(maxlen = 4)
                continue
            if ']' == char:
                # print('\tleaving square brackets')
                inside_square = False
                buffer = deque(maxlen = 4)
                continue
            buffer.append(char)
            if len(buffer) < 4:
                continue
            if is_abba(buffer):
                if inside_square:
                    # print("SKIP: line {0} has {1} in square brackets!".format(line, buffer))
                    this_has_abba = False
                    break
                else:
                    # print('ABBA: ', buffer)
                    this_has_abba = True
        if this_has_abba:
            total_abba += 1
        # print('COUNTER: ', total_abba)
print('Total ABBAs: ', total_abba)
