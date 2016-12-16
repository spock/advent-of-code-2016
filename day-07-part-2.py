# day 7 puzzle 2
import itertools
from collections import deque

def is_aba(s):
    return True if s[0] != s[1] and s[0] == s[2] else False

def is_bab_of_aba(bab, aba):
    return True if bab[0] == aba[1] and bab[1] == aba[0] else False

buffer_length = 3
total_ssl = 0
with open('day_7_puzzle_1.txt') as fh:
    for line in fh:
        line = line.strip()
        buffer = deque(maxlen = buffer_length)
        inside_square = False
        all_aba_outside = set()
        all_aba_inside = set()
        # print(line)
        for char in line:
            if '[' == char:
                # print('[')
                inside_square = True
                buffer = deque(maxlen = buffer_length)
                continue
            if ']' == char:
                # print(']')
                inside_square = False
                buffer = deque(maxlen = buffer_length)
                continue
            buffer.append(char)
            if len(buffer) < buffer_length:
                continue
            if is_aba(buffer):
                if inside_square:
                    all_aba_inside.add(''.join(buffer))
                    # print('ABA  inside:', ''.join(buffer))
                else:
                    all_aba_outside.add(''.join(buffer))
                    # print('ABA outside:', ''.join(buffer))
        if len(all_aba_inside) > 0 and len(all_aba_outside) > 0:
            for aba, bab in itertools.product(all_aba_outside, all_aba_inside):
                if is_bab_of_aba(bab, aba):
                    # print(bab, 'is a BAB of ABA', aba)
                    total_ssl += 1
                    break
        # print('COUNTER: ', total_ssl)
print('Total SSL: ', total_ssl)
