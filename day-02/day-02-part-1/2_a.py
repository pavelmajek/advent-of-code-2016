# Advent of Code 2016, day 2, part 1

import numpy

with open("../../data/2.txt") as file:
    instructions = [line.strip() for line in file.readlines()]

keypad = [i for i in range(1, 10)]
keypad = numpy.reshape(keypad, (3, 3))
code = []

keypad_index = (1, 1)
new_index = keypad_index
for instruction in instructions:
    index = 0
    while index < len(instruction):
        match instruction[index]:
            case "U":
                if keypad_index[0] - 1 < 0:
                    pass
                else:
                    new_index = (keypad_index[0] - 1, keypad_index[1])
            case "D":
                if keypad_index[0] + 1 > len(keypad) - 1:
                    pass
                else:
                    new_index = (keypad_index[0] + 1, keypad_index[1])
            case "L":
                if keypad_index[1] - 1 < 0:
                    pass
                else:
                    new_index = (keypad_index[0], keypad_index[1] - 1)
            case "R":
                if keypad_index[1] + 1 > len(keypad[0]) - 1:
                    pass
                else:
                    new_index = (keypad_index[0], keypad_index[1] + 1)
        keypad_index = new_index
        index += 1
    code.append(keypad[keypad_index[0]][keypad_index[1]])

print(f"Code:", *code)
