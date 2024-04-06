# Advent of Code 2016, day 9, part 1

import re

with open("../../data/9.txt") as file:
    sequence = file.read()

pattern = r"\((\d+)x(\d+)\)"
to_add = 0
start_index = 0
while True:
    match = re.search(pattern, sequence[start_index:])
    if match:
        first_integer = int(match.group(1))
        second_integer = int(match.group(2))
        match_length = match.end() - match.start()

        start_index += match.start() + match_length + first_integer
        to_add += (first_integer * (second_integer - 1)) - match_length
    else:
        break

decompressed = len(sequence) + to_add
print(f"Decompressed length: {decompressed}")
