# day4 puzzle 1
import re
from collections import defaultdict, Counter
from operator import itemgetter

sum_of_sectorids = 0
pattern = re.compile('([-a-z]+)-([0-9]+)\[([a-z]+)\]')
#with open('day_4_puzzle_1_test_input.txt') as fh:
with open('day_4_puzzle_1.txt') as fh:
    for line in fh:
        # extract room name with dashes, and make a version w/o dashes:
        # ababa-galamaga-1234[checksum]
        name, sectorid, checksum = pattern.match(line.strip()).groups()
        name = name.replace('-', '')
        sectorid = int(sectorid)
        # dict of counts {'a': count}
        counts = Counter(name)
        tuples = [(x, y) for x, y in counts.items()]
        #print('tuples:', tuples)
        # sort by alphabet
        tuples = sorted(tuples, key=itemgetter(0))
        #print('tuples alpha:', tuples)
        # sort by count descending, take top 5
        tuples = sorted(tuples, key=itemgetter(1), reverse=True)[0:5]
        #print('tuples counts:', tuples)
        most_frequent = ''.join([x[0] for x in tuples])
        #print(most_frequent, '<==>', checksum)
        # add up valid sectors' IDs
        if most_frequent == checksum:
            sum_of_sectorids += sectorid
print(sum_of_sectorids)
