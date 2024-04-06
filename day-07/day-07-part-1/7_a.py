# Advent of Code 2016, day 7, part 1

import re

with open("../../data/7.txt") as file:
    content = [line.strip() for line in file.readlines()]

count = 0
for line in content:
    if not any(re.search(r"(?=(\w)(?!\1)(\w)\2\1)\w{4}", bracket_content) for bracket_content in re.findall(r"\[(.*?)\]", line)):
        if re.search(r"(?=(\w)(?!\1)(\w)\2\1)\w{4}", line):
            count += 1
            print(line)

print(f"Count: {count}")
