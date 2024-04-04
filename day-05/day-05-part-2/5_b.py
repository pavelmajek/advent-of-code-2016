# Advent of Code 2016, day 5, part 2

import hashlib

my_key = "ffykfhsq"
n = 0
c = 0
code = {}
while c < 8:
    key_input = my_key + str(n)
    result = hashlib.md5(key_input.encode())
    if (result.hexdigest().startswith("00000")
            and result.hexdigest()[5].isdigit()
            and int(result.hexdigest()[5]) < 8
            and int(result.hexdigest()[5]) not in code):
        code[int(result.hexdigest()[5])] = result.hexdigest()[6]
        c += 1
    n += 1

for key in sorted(code.keys()):
    print(code[key], end="")
