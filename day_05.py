from utils import lines_to_arr
import pprint
from tqdm import tqdm

pp = pprint.PrettyPrinter(indent=4)

# PATH = "/home/shaun/src/advent-of-code-2023/day_05_test_input.txt"
PATH = "/home/shaun/src/advent-of-code-2023/day_05_input.txt"
lines = filter(lambda x: x != "", lines_to_arr(PATH))

# seeds: []
# maps : { name: "wat ever", rows: [{dest: num, src: num , len: num}]} }

# build base maps
base_maps = {}

for l in lines:
    if l.find("seeds") != -1:
        # seeds
        seeds =  [int(i) for i in l.split(":")[1].strip().split(" ")]
        continue
    if l.find("map") != -1:
        k = l.split(" ")[0]
        current_map_k = k
        continue
    [dest, src, length] =  [int(i) for i in l.split(" ")]
    rows = base_maps.get(current_map_k, [])
    rows.append({"dest": dest, "src": src, "length": length})
    base_maps[current_map_k] = rows
        
# pp.pprint(base_maps)

print("Building Base maps")
# seed is src  -> seed to src map
# {'dest': 50, 'length': 2, 'src': 98}

# final_map = {}

map_names = list(base_maps.keys())

# for mape_name in map_names:
#     map_values = {}
#     for m in base_maps[mape_name]:
#         for i in range(m["length"]):
#             k = i + m["src"]
#             v = i + m["dest"]
#             map_values[k] = v
    
#     final_map[mape_name]  = map_values


def fancy_seeds(seeds):
    print(seeds)
    arr = []
    
    for x in range(0, len(seeds), 2):
        seed = seeds[x]
        count = seeds[x+1]
        # print(f"Seed {seed}, count: {count}")
        for s in range(seed, seed+count):
            print(s)
            arr.append(s)
            # yield s

    return arr

def very_fancy_seeds(seeds):
    for x in range(0, len(seeds), 2):
        seed = seeds[x]
        count = seeds[x+1]
        for s in range(seed, seed+count):
            yield s

def get_value_from_map(key, value):
    maps = base_maps[key]
    # print(f"key value: {value}")
    for m in maps:
        # print(f"src: {m['src']}, value: {value}")
        diff = value - m["src"]
        # print(f"Diff: {diff}")
        if diff > -1 and diff <= m["length"]:
            # print(f'dest: {m["dest"]}"')
            return m["dest"] + diff
    
    return value
# pp.pprint(final_map)



lowest =  1E100
# total_seeds = 27
total_seeds = 1753244662
# SLOWWWWWWWWWWW - runtime -> 7:30:26

with tqdm(total=total_seeds) as pbar:
    for seed in very_fancy_seeds(seeds):
        # print(f"Seed: {seed}")
        value = seed
        counter = 0 
        current =  "seed"
        while current != "location":
            # find key that starts with current
            [m] = filter( lambda x: x.startswith(current), map_names )
            
            # value = final_map[m].get(value, value)
            
            value = get_value_from_map(m, value)
            [_, current] = m.split("-to-")
            
            # print(f"{current}: {value}")
            
            counter += 1
            if counter == 10:
                print("AHHHHHH Breaking ")
                break
            
        if value < lowest:
            lowest = value
        pbar.update(1)
        

# print("how many seeds")
# total = 0
# with tqdm(total=total_seeds) as pbar:
#     for i in very_fancy_seeds(seeds):
#         total += 1
#         pbar.update(1)
        
# print(f"${total}")

print(f"Lowest: {lowest}")
