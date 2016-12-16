# day 6 puzzles 1 and 2
from string import ascii_lowercase
from collections import Counter, defaultdict
from operator import itemgetter

columns = defaultdict(list)
answer = ''
with open('day_6_puzzle_1.txt') as fh:
    for line in fh:
        line = line.strip()
        #print(line)
        for i in range(len(line)):
            #print("appending %s to column %s" % (line[i], i))
            columns[i].append(line[i])

for col in columns.values():
    counts = Counter(col)  # dict of counts {'a': count}
    tuples = [(x, y) for x, y in counts.items()]
    # for puzzle 2: just remove reverse=True below
    tuples = sorted(tuples, key=itemgetter(1), reverse=True)[0]  # by count, the most abundand
    answer += tuples[0]

print(answer)
