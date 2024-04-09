# Advent of Code 2016, day 10, part 1

with open("../../data/10.txt") as file:
    instructions = [line.strip().split() for line in file.readlines()]

class Bot:
    def __init__(self, number):
        self.number = number
        self.chips = []
        self.low = {}
        self.high = {}


    def transfer_chips(self):
        min_chip = min(self.chips)
        max_chip = max(self.chips)
        for target, value in self.low.items():
            if target == "bot" and value not in bots:
                bots[value] = Bot(value)
            elif target == "output" and value not in outputs:
                outputs[value] = Output(value)
            if target == "bot":
                bots[value].receive_chip(min_chip)
            elif target == "output":
                outputs[value].receive_chip(min_chip)
        for target, value in self.high.items():
            if target == "bot" and value not in bots:
                bots[value] = Bot(value)
            elif target == "output" and value not in outputs:
                outputs[value] = Output(value)
            if target == "bot":
                bots[value].receive_chip(max_chip)
            elif target == "output":
                outputs[value].receive_chip(max_chip)
        self.chips = []

    def receive_chip(self, chip):
        self.chips.append(chip)

class Output:
    def __init__(self, number):
        self.number = number
        self.chips = []

    def receive_chip(self, chip):
        self.chips.append(chip)

bots = {}
outputs = {}

for instruction in instructions:
    if instruction[0] == "value":
        bot_number = int(instruction[-1])
        if bot_number not in bots:
            bots[bot_number] = Bot(bot_number)
        bots[bot_number].chips.append(int(instruction[1]))
    else:
        bot_number = int(instruction[1])
        if bot_number not in bots:
            bots[bot_number] = Bot(bot_number)
        bots[bot_number].low = {instruction[5]: int(instruction[6])}
        bots[bot_number].high = {instruction[-2]: int(instruction[-1])}

finished = False
while any(len(bot.chips) == 2 for bot in bots.values()) and not finished:
    for bot_number, bot in bots.items():
        if sorted(bot.chips) == [17, 61]:
            print(f"Bot number: {bot_number}")
            finished = True
            break
        if len(bot.chips) == 2:
            bot.transfer_chips()
            break
