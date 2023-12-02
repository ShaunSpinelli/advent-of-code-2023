def lines_to_arr(path):
    with open(path) as f:
        lines = f.readlines()
        return [l.strip() for l in lines]
