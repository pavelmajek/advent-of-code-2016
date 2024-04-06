# Advent of Code 2016, day 8, part 1

import numpy

screen = numpy.zeros((6, 50), int)

with open("../../data/8.txt") as file:
    instructions = [line.strip() for line in file.readlines()]

for instruction in instructions:
    if instruction.startswith("rect"):
        row = int(instruction.split()[1].split("x")[1])
        column = int(instruction.split()[1].split("x")[0])
        screen[:row, :column] = 1

    elif instruction.startswith("rotate row"):
        screen_copy = screen.copy()
        row = int(instruction.split()[-3].split("=")[1])
        shift = int(instruction.split()[-1])
        for i in range(len(screen[0])):
            screen_copy[row][(i + shift) % len(screen[0])] = screen[row][i]
        screen = screen_copy

    elif instruction.startswith("rotate column"):
        screen_copy = screen.copy()
        column = int(instruction.split()[-3].split("=")[1])
        shift = int(instruction.split()[-1])
        for i in range(len(screen)):
            screen_copy[(i + shift) % len(screen)][column] = screen[i][column]
        screen = screen_copy

print(f"Pixels lit: {numpy.sum(screen)}")
