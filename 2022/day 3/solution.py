# mode = "test"
mode = "prod"

if mode == "test":
    inpath = "test_data.txt"
else:
    inpath = "input.txt"


def parse_line(line: str):
    length = int(len(line)/2)
    part_one = line[:length]
    part_two = line[length:]
    part_one_set = set(part_one)
    part_two_set = set(part_two)
    overlap = part_one_set.intersection(part_two_set)
    return part_one, part_two, str(overlap)

# part 1
def score_overlap(overlap: str):
    total = 0
    for letter in overlap:
        if letter.islower():
            # ord("a") = 97
            total += ord(letter) - 96
        elif letter.isupper():
            # ord("A") = 65
            total += ord(letter) - 38
    if total < 0:
        print(overlap)
    return total


rucksacks = list()
total = 0
with open(inpath) as infile:
    for line in infile:
        line = line.strip()
        part_one, part_two, overlap = parse_line(line)
        score = score_overlap(overlap)
        total += score

print(total)


# part 2

def find_common(lines):
    set_one = set(lines[0])
    set_two = set(lines[1])
    set_three = set(lines[2])
    overlap1 = set_one.intersection(set_two)
    final = overlap1.intersection(set_three)
    return str(final)


total = 0
accumulator = list()
with open(inpath) as infile:
    for line in infile:
        if len(accumulator) >= 3:
            badge = find_common(accumulator)
            score = score_overlap(badge)
            total += score
            accumulator = list()
        accumulator.append(line.strip())
    if accumulator:
        badge = find_common(accumulator)
        score = score_overlap(badge)
        total += score
print(total)