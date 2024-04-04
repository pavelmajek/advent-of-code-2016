# Advent of Code 2016, day 4, part 1

from collections import Counter

with open("../../data/4.txt") as file:
    codes = [line.strip() for line in file.readlines()]

total = 0
for code in codes:
    letter_counts = Counter(char for char in code[:-10] if char.isalpha())
    sorted_counts = sorted(letter_counts.items(), key=lambda item: (-item[1], item[0]))
    count_string = "".join(x[0] for x in sorted_counts[:5])
    if code[-6:-1] == count_string:
        total += int(code[-10:-7])

print(f"Sum: {total}")
