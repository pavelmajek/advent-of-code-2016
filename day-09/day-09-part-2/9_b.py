# Advent of Code 2016, day 9, part 2

import re

with open("../../data/9.txt") as file:
    content = file.read().strip()

pattern = r"\((\d+)x(\d+)\)"


def decompress(sequence):
    match = re.search(pattern, sequence)

    if match:
        first = int(match.group(1))
        second = int(match.group(2))
        index = match.end()
        return len(sequence[:match.start()]) + decompress(sequence[index:index + first]) * second + decompress(sequence[index + first:])
    else:
        return len(sequence)


print(f"Decompressed length: {decompress(content)}")
