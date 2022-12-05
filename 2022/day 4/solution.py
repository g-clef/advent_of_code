from typing import Set

# mode = "test"
mode = "prod"

if mode == "test":
    inpath = "test_data.txt"
else:
    inpath = "input.txt"


def make_range(assignment):
    start, end = assignment.split("-")
    start = int(start)
    end = int(end)
    return set(range(start, end+1))


jobs = list()
with open(inpath) as infile:
    for line in infile:
        line = line.strip()
        first, second = line.split(",")
        jobs.append((make_range(first), make_range(second)),)

# part 1
def does_enclose(first: Set, second: Set):
    if first.issubset(second):
        return True
    elif second.issubset(first):
        return True
    return False


overlapping = sum([1 if does_enclose(first, second) else 0 for first, second in jobs])
print(overlapping)


# part 2
def does_overlap(first: Set, second: Set):
    if first.intersection(second):
        return True
    return False

overlapping = sum([1 if does_overlap(first, second) else 0 for first, second in jobs])
print(overlapping)
