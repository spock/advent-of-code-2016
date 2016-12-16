# 2016-12-01, first
route = 'R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3'
route_list = route.split(', ')
facing = 'N'  # we start at 0, 0 facing North/up
coords = {'x':0, 'y':0}  # keep track of x and y coordinates
# map all input facing directions together with R/L turn to all output facing directions, step_map[facing][turn] = new_facing
step_map = {'N': {'R':'E', 'L':'W'}, 'E': {'R':'S', 'L':'N'}, 'W': {'R':'N', 'L': 'S'}, 'S':{'R':'W', 'L':'E'}}

for step in route_list:
    #print('facing ', facing)
    turn, distance = step[0:1], int(step[1:])
    #print('turn "%s", distance "%s"' % (turn, distance))
    facing = step_map[facing][turn]
    #print('facing ', facing)
    if facing == 'N':
        coords['y'] += distance  #; print('increased Y by', distance)
    elif facing == 'E':
        coords['x'] += distance  #; print('increased X by', distance)
    elif facing == 'S':
        coords['y'] -= distance  #; print('decreased Y by', distance)
    elif facing == 'W':
        coords['x'] -= distance  #; print('decreased X by', distance)

print('final coordinates:', coords)
print('distance to origin:', abs(coords['x']) + abs(coords['y']))
