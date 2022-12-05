import copy

from collections import defaultdict
from typing import DefaultDict, List

# mode = "test"
mode = "prod"

if mode == "test":
    # note: make sure spaces exist for each column. Pycharm eats end-of-line spaces by default.
    inpath = "test_data.txt"
else:
    inpath = "input.txt"


def chunk_line(line, chunksize=4):
    # split the string into multiple "chunksize" blocks
    return (line[0+i:chunksize+i] for i in range(0, len(line), chunksize))


def parse_stack_line(line):
    return [entry.strip() for entry in chunk_line(line)]

stacks = defaultdict(list)
raw_stacks = None
commands = list()
with open(inpath) as infile:
    mode = "stack"
    for line in infile:
        line = line.strip("\n")
        if mode == "stack" and "[" not in line:
            # this is the stack identifiers
            ids = line.split()
            for counter in range(len(ids)):
                stacks[ids[counter]] = raw_stacks[counter]
            mode = "commands"
            continue
        if not line.strip():
            continue
        if mode == "stack":
            crates = parse_stack_line(line)
            if raw_stacks is None:
                raw_stacks = [[] for _ in range(len(crates))]
            for counter in range(len(crates)):
                if crates[counter]:
                    raw_stacks[counter].insert(0, crates[counter])
        elif mode == "commands":
            commands.append(line)

print(stacks)

part_one_stacks = copy.copy(stacks)
# part 1
def handle_line(stacks: DefaultDict[str, List[str]], command: str):
    _, num_to_move, _, from_stack, _, to_stack = command.split()
    num_to_move = int(num_to_move)
    stuff_to_move = stacks[from_stack][-1 * num_to_move:]
    stacks[from_stack] = stacks[from_stack][:-1 * num_to_move]
    stuff_to_move.reverse()
    stacks[to_stack] = stacks[to_stack] + stuff_to_move


for line in commands:
    handle_line(part_one_stacks, line)

print("part 1")
for stack in part_one_stacks:
    print(f"{stack}, {part_one_stacks[stack][-1]}")

# part 2
part_two_stacks = copy.copy(stacks)


def handle_part_two_line(stacks: DefaultDict[str, List[str]], command: str):
    _, num_to_move, _, from_stack, _, to_stack = command.split()
    num_to_move = int(num_to_move)
    stuff_to_move = stacks[from_stack][-1 * num_to_move:]
    stacks[from_stack] = stacks[from_stack][:-1 * num_to_move]
    stacks[to_stack] = stacks[to_stack] + stuff_to_move

for line in commands:
    handle_part_two_line(part_two_stacks, line)

print("part 2")
for stack in part_two_stacks:
    print(f"{stack}, {part_two_stacks[stack][-1]}")