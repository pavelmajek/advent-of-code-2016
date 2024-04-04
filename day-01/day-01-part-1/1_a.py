# Advent of Code 2016, day 1, part 1

with open("../../data/1.txt") as file:
    content = file.read().strip().split(", ")

x_blocks = []
y_blocks = []

vector = 0
index = 0
while index < len(content):
    if vector == 0:
        x_blocks.append(int(content[index][1:]) if content[index][0] == "R" else -int(content[index][1:]))
    elif vector == 2:
        x_blocks.append(-int(content[index][1:]) if content[index][0] == "R" else int(content[index][1:]))
    elif vector == 1:
        y_blocks.append(int(content[index][1:]) if content[index][0] == "R" else -int(content[index][1:]))
    elif vector == 3:
        y_blocks.append(-int(content[index][1:]) if content[index][0] == "R" else int(content[index][1:]))

    vector = (vector + (1 if content[index][0] == "R" else -1)) % 4
    index += 1

print(f"Distance: {abs(sum(x_blocks)) + abs(sum(y_blocks))}")
