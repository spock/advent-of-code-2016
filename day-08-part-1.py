# day 8, part 1
# 50 pixels wide and 6 pixels tall, all of which start "off" - guess it's time to learn some numpy arrays.
# As this is my first numpy experience, code is likely suboptimal.
import numpy as np
import re

# test input:
# width = 7
# height = 3

width = 50
height = 6
# It would be nicer to have "Screen" object with manipulation methods, and a nice printing function.
screen = np.zeros((height, width), dtype=np.int16)

def rect(screen, a, b):
    """rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall."""
    screen[0:b, 0:a] = 1
    return screen

def rotate_row(screen, row, pixels):
    """Shifts all of the pixels in "row" (0 is the top row) right by "pixels".
    Pixels that would fall off the right end appear at the left end of the row."""
    row_old = screen[row, :]
    row_new = np.roll(row_old, pixels)  # no axis for 1D
    screen[row, :] = row_new
    return screen

def rotate_column(screen, column, pixels):
    """Shifts all of the pixels in "column" (0 is the leftmost column) down by "pixels".
    Pixels that would fall off the bottom appear at the top of the column."""
    column_old = screen[:, column]
    column_new = np.roll(column_old, pixels)  # no axis for 1D
    screen[:, column] = column_new
    return screen

rect_pat = re.compile('rect ([0-9]+)x([0-9]+)')  # rect 3x2
row_pat = re.compile('rotate row y=([0-9]+) by ([0-9]+)')  # rotate row y=0 by 4
col_pat = re.compile('rotate column x=([0-9]+) by ([0-9]+)')  # rotate column x=1 by 1

#with open('day_8_puzzle_1_test.txt') as fh:
with open('day_8_puzzle_1.txt') as fh:
    for line in fh:
        line = line.strip()
        if line.startswith('rotate row'):
            row, pixels = map(int, row_pat.match(line).groups())
            screen = rotate_row(screen, row, pixels)
        elif line.startswith('rotate column'):
            column, pixels = map(int, col_pat.match(line).groups())
            screen = rotate_column(screen, column, pixels)
        elif line.startswith('rect'):
            a, b = map(int, rect_pat.match(line).groups())
            screen = rect(screen, a, b)

total_pixels = screen.sum()
print("Total enabled pixels: ", total_pixels)
# print(screen)
