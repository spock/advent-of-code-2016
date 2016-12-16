# day 3 puzzle 2: 3 numbers in a column form a triangle, valid for all 3 columns
possible_triangles = 0

def is_triangle(s1, s2, s3):
    """Return 1 if sides s1, s2, s3 may belong to a triangle, and 0 otherwise."""
    if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
        return 1
    else:
        return 0

rows_counter = 0  # keep track of row triplets
triplets = {1: [], 2: [], 3: []}  # maintain a list of sides for each column
with open('day_3_puzzle_1.txt') as fh:
    for line in fh:
        rows_counter += 1
        c1, c2, c3 = map(int, line.strip().split())
        triplets[1].append(c1)
        triplets[2].append(c2)
        triplets[3].append(c3)
        if rows_counter == 3:
            # all triplets should be complete: test for triangles, reset counter/triplets
            possible_triangles += is_triangle(*triplets[1])
            possible_triangles += is_triangle(*triplets[2])
            possible_triangles += is_triangle(*triplets[3])
            rows_counter = 0
            triplets = {1: [], 2: [], 3: []}

print(possible_triangles)
