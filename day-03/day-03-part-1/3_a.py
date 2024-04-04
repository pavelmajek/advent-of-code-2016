# Advent of Code 2016, day 3, part 1

with open("../../data/3.txt") as file:
    lines = [line.strip().split() for line in file.readlines()]

triangles = [(int(line[0]), int(line[1]), int(line[2])) for line in lines]
count = 0
for triangle in triangles:
    if sorted(triangle)[-1] < sorted(triangle)[0] + sorted(triangle)[1]:
        count += 1

print(f"Triangles: {count}")
