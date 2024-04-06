# Advent of Code 2016, day 7, part 2

import re

with open("../../data/7.txt") as file:
    content = [line.strip() for line in file.readlines()]

count = 0
for line in content:
    found = False
    bracket_contents = re.findall(r"\[(.*?)\]", line)
    outside_brackets = re.split(r"\[.*?\]", line)

    for sequence in outside_brackets:
        for i in range(len(sequence) - 2):
            if sequence[i] == sequence[i + 2] and sequence[i] != sequence[i + 1]:
                aba = sequence[i:i + 3]
                bab = aba[1] + aba[0] + aba[1]
                for seq in bracket_contents:
                    if bab in seq:
                        found = True
    if found:
        count += 1

print(f"Count: {count}")
