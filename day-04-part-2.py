# day4 puzzle 2
import re
from collections import defaultdict, Counter
from operator import itemgetter
from string import ascii_lowercase

def decrypt(name, sectorid):
    real_name = ''
    for letter in name:
        if '-' == letter:
            real_name += ' '
        else:
            new_letter_index = (ascii_lowercase.index(letter) + sectorid) % len(ascii_lowercase)
            real_name += ascii_lowercase[new_letter_index]
    return real_name

sum_of_sectorids = 0
# ababa-galamaga-1234[checksum_string]
pattern = re.compile('([-a-z]+)-([0-9]+)\[([a-z]+)\]')
#with open('day_4_puzzle_1_test_input.txt') as fh:
with open('day_4_puzzle_1.txt') as fh:
    for line in fh:
        name, sectorid, checksum = pattern.match(line.strip()).groups()
        name_nodashes = name.replace('-', '')
        sectorid = int(sectorid)
        counts = Counter(name_nodashes)  # dict of counts {'a': count}
        tuples = [(x, y) for x, y in counts.items()]
        tuples = sorted(tuples, key=itemgetter(0))  # by alphabet
        tuples = sorted(tuples, key=itemgetter(1), reverse=True)[0:5]  # sort by count descending, take top 5
        most_frequent = ''.join([x[0] for x in tuples])
        if most_frequent == checksum:
            real_name = decrypt(name, sectorid)
            if 'north' in real_name:
                print('= = = = = = = = = = = = = = = = = = = = = = = =')
            print(real_name, sectorid)
