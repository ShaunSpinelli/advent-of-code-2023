from utils import lines_to_arr
import random

# Time:      7  15   30
# Distance:  9  40  200

# PATH = "/home/shaun/src/advent-of-code-2023/day_07_test_input.txt"
PATH = "/home/shaun/src/advent-of-code-2023/day_07_input.txt"
lines = lines_to_arr(PATH)


# 5- 5 of kind
# 4 - 4 of kind
# 3 - full house (3,2)
# 2 - 2 pair
# 1 - 1 pair
# 0 - high card

# A, K, Q, J, T
# 14,13,12,11,10


# wrong JQ9QK

def hand_to_score(hand):
    # 32T3K
    cards = {}

    hand_number = ""
    for h in hand:
        if h != "J": # We ignore J
            cards[h] = cards.get(h, 0) + 1
        if h == "A":
            hand_number += "14"
        elif h == "K":
            hand_number += "13"
        elif h == "Q":
            hand_number += "12"
        elif h == "J":
            hand_number += "00"
        elif h == "T":
            hand_number += "10"
        else:
            hand_number += "0" + h

    scores = list(cards.values())

    score = 1
    j_count = hand.count("J")
    if scores.count(5) > 0:
        score = 7 # stays 5
    elif scores.count(4) > 0:
        score = 6 + j_count
    elif scores.count(3) > 0 and scores.count(2):
        score = 5 + j_count + 1 
    elif scores.count(3) > 0:
        score = 4 + j_count + 1 # cause 4 is better then FH
    elif scores.count(2) == 2:
        if j_count == 1:
            score = 5  # FH
        else:
            score = 3 + j_count
    elif scores.count(2) > 0:
        if j_count == 0: score = 2
        if j_count == 1: score = 4
        if j_count > 1 : score = 2 + j_count + 2
    else:
        score = 1 + j_count
    
    if j_count > 0: print(f"Hand: {hand}  score:{score}")
    
    return int(str(score) + hand_number)


hands = []

lengths = []

for l in lines:
    [hand, bet] = l.split(" ")
    # print(f"hand: {hand}, bet: {bet}")
    hand_score = hand_to_score(hand)
    lengths.append(len(str(hand_score)))
    hands.append({"score": hand_score, "bet": int(bet)})


# sort
hands.sort(key=lambda x: x["score"])


# score
total = 0
for i, h in enumerate(hands):
    total += (i + 1) * h["bet"]


# print(hands)
print(total)

# 252295678
# 251265446
# 251319112
# 251525500
# 251852388

# 251963912
# 250618820
# 250910850