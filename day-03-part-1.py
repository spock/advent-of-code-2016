# day 3 puzzle 1
possible_triangles = 0
with open('day_3_puzzle_1.txt') as fh:
    for line in fh:
        s1, s2, s3 = map(int, line.strip().split())
        if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
            possible_triangles += 1
print(possible_triangles)
