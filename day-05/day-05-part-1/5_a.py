# Advent of Code 2016, day 5, part 1

import hashlib

my_key = "ffykfhsq"
n = 0
code = []
while len(code) < 8:
    key_input = my_key + str(n)
    result = hashlib.md5(key_input.encode())
    if result.hexdigest().startswith("00000"):
        code.append(result.hexdigest()[5])
    n += 1

print(f"Code: ", *code)
