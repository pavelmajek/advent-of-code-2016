# Advent of Code 2016, day 3, part 2

with open("../../data/3.txt") as file:
    lines = [line.strip().split() for line in file.readlines()]

triangles = []
for k in range(0, len(lines), 3):
    temp = [[row[i] for row in lines[k:k + 3]] for i in range(len(lines[0]))]
    for item in temp:
        triangles.append(item)

triangles = [(int(line[0]), int(line[1]), int(line[2])) for line in triangles]
count = 0
for triangle in triangles:
    if sorted(triangle)[-1] < sorted(triangle)[0] + sorted(triangle)[1]:
        count += 1

print(f"Triangles: {count}")
