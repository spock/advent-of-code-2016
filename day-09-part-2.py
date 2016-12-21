#!/usr/bin/python3
# day 9 part 2
import re

# Sum of all decompressed string lengths.
total_size = 0
header_pattern = re.compile('\(([0-9]+)x([0-9]+)\)')

def decompress(line):
    """
    Given a `line`, decompress it (and any nested blocks),
    keeping track of the total length of decompressed string.
    Return total length.
    """
    global header_pattern
    total_length = 0
    header_start = line.find('(')
    if -1 == header_start:
        # No compressed blocks until the end of the string
        total_length += len(line)
        return total_length
    else:
        # print('header start:', line[header_start:header_start + 1])
        if header_start > 0:
            # Count anything before the compressed data block
            total_length += header_start
        header_end = line.find(')')
        assert -1 != header_end
        # print('header end:', line[header_end:header_end + 1])
        block_length, block_repeat = map(int, header_pattern.match(line[header_start:]).groups())
        # print('block length and repeat for {0} are {1} and {2}'.format(line[header_start:header_end + 1],
        #                                                                block_length,
        #                                                                block_repeat))
        header_end += 1  # for the closing brace )
        total_length += decompress(line[header_end:header_end + block_length]) * block_repeat
        total_length += decompress(line[header_end + block_length:])
        return total_length

# print('input\t\t\tlength')
with open('day_9_part_1.txt') as fh:
    for line in fh:
        line = line.strip()
        line_length = decompress(line)
        # print('{0}\t\t\t{1}'.format(line, line_length))
        total_size += line_length

print('Total size of all decompressed strings: ', total_size)

