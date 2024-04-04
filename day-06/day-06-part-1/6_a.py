# Advent of Code 2016, day 6, part 1

from collections import Counter

with open("../../data/6.txt") as file:
    content = [line.strip() for line in file.readlines()]

columns = [[row[i] for row in content] for i in range(len(content[0]))]
code = ''.join(Counter(item).most_common(1)[0][0] for item in columns)

print(code)
