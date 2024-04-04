# Advent of Code 2016, day 4, part 2

import string
from collections import Counter

with open("../../data/4.txt") as file:
    codes = [line.strip() for line in file.readlines()]

real = []
total = 0
for code in codes:
    letter_counts = Counter(char for char in code[:-10] if char.isalpha())
    sorted_counts = sorted(letter_counts.items(), key=lambda item: (-item[1], item[0]))
    count_string = "".join(x[0] for x in sorted_counts[:5])
    if code[-6:-1] == count_string:
        real.append(code[:-7].replace("-", " "))

for code in real:
    decrypted = ""
    for char in code[:-3]:
        decrypted += string.ascii_lowercase[(string.ascii_lowercase.index(char) + int(code[-3:])) % len(string.ascii_lowercase)] if char.isalpha() else " "
    if "north" in decrypted:
        print(f"Sector ID: {code[-3:]}")
