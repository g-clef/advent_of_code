
# mode = "testing"
mode = "prod"

if mode == "testing":
    inpath = "test_data.txt"
else:
    inpath = "input.txt"

# A = Rock, X = Rock
# B = Paper, Y = Paper
# C = Scissors, Z = Scissors

# Part 1
def score_play(opp, you):
    score = you
    if opp == you:
        score += 3
    if you - opp == 1:
        score += 6
    if opp == 3 and you == 1:
        score += 6
    return score


calls = list()
with open(inpath) as infile:
    for line in infile:
        line = line.strip()
        opp, you = line.split(" ")
        # translate to numbers
        you = ord(you) - ord("W")
        opp = ord(opp) - ord("@")

        calls.append((opp, you),)
total = sum([score_play(opp, you) for opp, you in calls])
print(total)

# part 2
def score_second_play(opp, you):
    # you: 1 = lose, 2 = draw, 3 = win
    if you == 1:
        choice = opp - 1
        if choice == 0:
            choice = 3
        score = choice
    elif you == 2:
        score = 3 + opp
    elif you == 3:
        choice = opp + 1
        if choice == 4:
            choice = 1
        score = 6 + choice
    else:
        raise
    return score

total = sum([score_second_play(opp, you) for opp, you in calls])
print(total)