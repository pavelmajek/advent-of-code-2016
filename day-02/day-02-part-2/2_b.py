# Advent of Code 2016, day 2, part 2

with open("../../data/2.txt") as file:
    instructions = [line.strip() for line in file.readlines()]

keypad = {"1": (0, 2), "2": (1, 1), "3": (1, 2), "4": (1, 3), "5": (2, 0), "6": (2, 1), "7": (2, 2), "8": (2, 3), "9": (2, 4), "A": (3, 1), "B": (3, 2), "C": (3, 3), "D": (4, 2)}
code = []
keypad_index = (2, 0)
new_index = keypad_index
for instruction in instructions:
    index = 0
    while index < len(instruction):
        match instruction[index]:
            case "U":
                if (keypad_index[0] - 1, keypad_index[1]) not in keypad.values():
                    pass
                else:
                    new_index = (keypad_index[0] - 1, keypad_index[1])
            case "D":
                if (keypad_index[0] + 1, keypad_index[1]) not in keypad.values():
                    pass
                else:
                    new_index = (keypad_index[0] + 1, keypad_index[1])
            case "L":
                if (keypad_index[0], keypad_index[1] - 1) not in keypad.values():
                    pass
                else:
                    new_index = (keypad_index[0], keypad_index[1] - 1)
            case "R":
                if (keypad_index[0], keypad_index[1] + 1) not in keypad.values():
                    pass
                else:
                    new_index = (keypad_index[0], keypad_index[1] + 1)
        keypad_index = new_index
        index += 1
    for key, value in keypad.items():
        if value == keypad_index:
            code.append(key)

print(f"Code: ", *code)
