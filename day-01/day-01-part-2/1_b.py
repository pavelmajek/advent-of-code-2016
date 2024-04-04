# Advent of Code 2016, day 1, part 2

with open("../../data/1.txt") as file:
    content = file.read().strip().split(", ")

x_blocks = []
y_blocks = []
positions = []
start_position = (0, 0)
vector = 0
index = 0
final = None
while index < len(content):
    if vector == 0:
        x = (int(content[index][1:]) if content[index][0] == "R" else -int(content[index][1:]))
        x_blocks.append(x)
        new_position = (start_position[0] + x, start_position[1])
        for i in range(abs(x)):
            upload_position = (start_position[0] + i, start_position[1]) if content[index][0] == "R" else (start_position[0] - i, start_position[1])
            if upload_position in positions:
                final = upload_position
            else:
                positions.append(upload_position)

    elif vector == 2:
        x = (-int(content[index][1:]) if content[index][0] == "R" else int(content[index][1:]))
        x_blocks.append(x)
        new_position = (start_position[0] + x, start_position[1])
        for i in range(abs(x)):
            upload_position = (start_position[0] - i, start_position[1]) if content[index][0] == "R" else (start_position[0] + i, start_position[1])
            if upload_position in positions:
                final = upload_position
            else:
                positions.append(upload_position)

    elif vector == 1:
        y = (int(content[index][1:]) if content[index][0] == "R" else -int(content[index][1:]))
        y_blocks.append(y)
        new_position = (start_position[0], start_position[1] + y)
        for i in range(abs(y)):
            upload_position = (start_position[0], start_position[1] + i) if content[index][0] == "R" else (start_position[0], start_position[1] - i)
            if upload_position in positions:
                final = upload_position
            else:
                positions.append(upload_position)

    elif vector == 3:
        y = (-int(content[index][1:]) if content[index][0] == "R" else int(content[index][1:]))
        y_blocks.append(y)
        new_position = (start_position[0], start_position[1] + y)
        for i in range(abs(y)):
            upload_position = (start_position[0], start_position[1] - i) if content[index][0] == "R" else (start_position[0], start_position[1] + i)
            if upload_position in positions:
                final = upload_position
            else:
                positions.append(upload_position)

    vector = (vector + (1 if content[index][0] == "R" else -1)) % 4
    start_position = new_position
    index += 1

    if final is not None:
        break

print(f"Distance: {abs(final[0]) + abs(final[1])}")
