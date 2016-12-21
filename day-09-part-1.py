#!/usr/bin/python3
# day 9 part 1
import re

# Sum of all decompressed string lengths.
total_size = 0
header_pattern = re.compile('\(([0-9]+)x([0-9]+)\)')

with open('day_9_part_1.txt') as fh:
    for line in fh:
        line = line.strip()
        #print('input: ', line)
        # Final decompressed string.
        decompressed = ''
        # Stream processing is a bit too complicated here, will instead use coordinates-based approach.
        current_coord = 0
        while current_coord < len(line):
            #print('current coordinate: ', current_coord)
            header_start = line.find('(', current_coord)
            if -1 == header_start:
                #print('No compressed blocks until the end of the string')
                decompressed += line[current_coord:]
                current_coord = len(line)
            else:
                #print('header start:', line[header_start:header_start + 1])
                if header_start > current_coord:
                    #print('append anything before the compressed data block: ', line[current_coord:header_start])
                    decompressed += line[current_coord:header_start]
                header_end = line.find(')', header_start)
                assert -1 != header_end
                #print('header end:', line[header_end:header_end + 1])
                block_length, block_repeat = map(int, header_pattern.match(line[header_start:]).groups())
                #print('block length and repeat for {0} are {1} and {2}'.format(line[header_start:header_end + 1],
                #                                                              block_length,
                #                                                              block_repeat))
                
                current_coord = header_end + 1 + block_length
                decompressed += line[header_end + 1: current_coord] * block_repeat
            #print('decompressed so far: ', decompressed)
            #print('remaining string:', line[current_coord:])
        #print(line, len(line), decompressed, len(decompressed))
        #print()
        total_size += len(decompressed)

print('Total size of all decompressed strings: ', total_size)
