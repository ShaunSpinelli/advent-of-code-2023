from utils import lines_to_arr

PATH = "day_01_input.txt"
# PATH = "test_input.txt"

NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# NUMBERS = list(NUMBER_MAP.keys())

NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


# def get_str_number_idx(string):
# returns number and index


def get_first_last_number_(string):
    first = None
    last = None

    for n in NUMBERS:
        string = string.replace(n, str(NUMBER_MAP[n]))

    for char in string:
        try:
            value = int(char)
            if first is None:
                first = value
            last = value

        except ValueError:
            continue

    # return int(f"{first}{last}")
    return int(f"{first}{first}")


def get_first_last_number(string):
    first = {"value": None, "idx": None}
    last = {"value": None, "idx": None}

    str_num_idxs = [string.find(n) for n in NUMBERS]

    for i, str_idx in enumerate(str_num_idxs):
        if str_idx == -1:
            continue
        if last["idx"] is None or str_idx > last["idx"]:
            last["value"] = i + 1
            last["idx"] = str_idx
        if first["value"] is None or str_idx < first["idx"]:
            first["value"] = i + 1
            first["idx"] = str_idx

    for idx, char in enumerate(string):
        try:
            value = int(char)
            if last["idx"] is None or idx > last["idx"]:
                last["value"] = value
                last["idx"] = idx
            if first["value"] is None or idx < first["idx"]:
                first["value"] = value
                first["idx"] = idx

        except ValueError:
            continue

    return int(f'{first["value"]}{last["value"]}')


items = lines_to_arr(PATH)

print(sum([get_first_last_number(i) for i in items]))
# wrong 54256
# 54256
# 54256
