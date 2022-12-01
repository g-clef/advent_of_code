from collections import deque

#mode = "testing"
mode = "prod"

if mode == "testing":
    inpath = "test_data.txt"
else:
    inpath = "input.txt"

# part 1
accumulator = 0
elves = list()
with open(inpath) as infile:
    for line in infile:
        line = line.strip()
        if not line:
            elves.append(accumulator)
            accumulator = 0
            continue
        line = int(line)
        accumulator += line
    if accumulator:
        elves.append(accumulator)

print(max(elves))

# part 2
TOP_X = 3
top_three = deque()
for elf in elves:
    top_three.append(elf)
    top_three = sorted(top_three, reverse=True)
    while len(top_three) > 3:
        top_three.pop()

print(sum(top_three))