from utils import lines_to_arr

# 12 red cubes, 13 green cubes, and 14 blue
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

PATH = "/home/shaun/src/advent-of-code-2023/day_02_input.txt"


def line_to_game(line):
    [id_str, games_str] = line.split(":")
    id = int(id_str.split(" ")[-1])

    game = {"id": id, "draws": []}

    draws = [d.strip() for d in games_str.split(";")]
    print(draws)
    for d in draws:
        draw = {}
        cols = d.split(",")
        for c in cols:
            num, colour = c.strip().split(" ")
            draw[colour] = int(num)
        game["draws"].append(draw)

    return game


games = [line_to_game(l) for l in lines_to_arr(PATH) if l]


# Part 1
good_games_count = 0

for game in games:
    bad = False
    print(f'Running game {game["id"]}')
    for draw in game["draws"]:
        print(draw)
        if draw.get("red", 0) > MAX_RED:
            bad = True
            break
        if draw.get("green", 0) > MAX_GREEN:
            bad = True
            break
        if draw.get("blue", 0) > MAX_BLUE:
            bad = True
            break
    print(f'Good game {game["id"]}')
    if not bad:
        good_games_count += game["id"]

print(good_games_count)


# Part 2
mults = []

for game in games:
    max_red = 0
    max_green = 0
    max_blue = 0

    print(f'Running game {game["id"]}')
    for draw in game["draws"]:
        print(draw)
        if draw.get("red", 0) > max_red:
            max_red = draw["red"]
        if draw.get("green", 0) > max_green:
            max_green = draw["green"]
        if draw.get("blue", 0) > max_blue:
            max_blue = draw["blue"]

    mults.append(max_red * max_green * max_blue)

print(sum(mults))
