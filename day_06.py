from utils import lines_to_arr
from math import prod
import pprint
from tqdm import tqdm

pp = pprint.PrettyPrinter(indent=4)


# Time:      7  15   30
# Distance:  9  40  200

# PATH = "/home/shaun/src/advent-of-code-2023/day_05_test_input.txt"
PATH = "/home/shaun/src/advent-of-code-2023/day_06_input.txt"
lines = lines_to_arr(PATH)


# (time - hold ) * hold

winning_counts = []
# part 1
races = [[40, 233], [82, 1011], [84, 1110], [92, 1487]]

# part 2
races = [[40828492, 233101111101487]]

for time, max_dist in races:
    winning_dist_cont = 0
    for hold in tqdm(range(1, time + 1)):
        dist = (time - hold) * hold
        if dist > max_dist:
            winning_dist_cont += 1
    winning_counts.append(winning_dist_cont)

print(winning_counts)
