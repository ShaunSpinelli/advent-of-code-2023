from utils import lines_to_arr
import uuid


PATH = "/home/shaun/src/advent-of-code-2023/day_04_test_input.txt"
# PATH = "/home/shaun/src/advent-of-code-2023/day_04_input.txt"
lines = lines_to_arr(PATH)


# Part 1
# total = 0

# for line in lines:
#     line_score = 0
#     w, m = line.split("|")
#     winning_numbers = [ i for i in w.split(":")[1].strip().split(" ") if i != ""]
#     mine = [ i for i in m.strip().split(" ") if i != ""]

#     # print(winning_numbers)
#     # print(mine)

#     for num in winning_numbers:
#         try:
#             mine.index(num) # raises if not found
#             if line_score == 0:
#                 line_score = 1
#             else:
#                 line_score = line_score * 2
#         except ValueError:
#             pass
#     total += line_score

# print(f"line Score: {total}")


# Part 2
total = 0

max = 1

games_count = {1: 1}

for c, line in enumerate(lines):
    game = c + 1
    wins = 0
    w, m = line.split("|")
    winning_numbers = [i for i in w.split(":")[1].strip().split(" ") if i != ""]
    mine = [i for i in m.strip().split(" ") if i != ""]

    # print(winning_numbers)
    # print(mine)

    for num in winning_numbers:
        try:
            mine.index(num)  # raises if not found
            wins += 1
        except ValueError:
            pass
    # if wins == 0: break # we dont want to check 0 we need to carry on going if we have won additional tickets
    print(f"Game {game}")
    print(f"wins: {wins} ")
    for i in range(wins):
        k = i + game + 1  # next game
        current = games_count.get(k, 0)  # always start with one cause its the original
        if current == 0:
            current += 2  # one for original and one for copy

        mulitplier = games_count[game]
        # print(current)
        print(f"k={k} current={current} mulitplier={mulitplier}")

        games_count[k] = (current + 1) * mulitplier
    if game == 3:
        break
    print(f"{list(games_count.values())}")
    print("")
    # print(f"Game {c}: wins: {wins}", )

# print(games_count.values())
# print("{1 2 4 8 15 6}")

print(f"Final Score: {sum(games_count.values())}")


c = """
 Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
 Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
 Your copy of card 2 also wins one copy each of cards 3 and 4.
 
 
 Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
 Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
 Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
 Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
 
 
 
 w = 2 cards original and copy
 
 """
