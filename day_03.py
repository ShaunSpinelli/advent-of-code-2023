from utils import lines_to_arr
import uuid


PATH = "/home/shaun/src/advent-of-code-2023/day_03_test_input.txt"
# PATH = "/home/shaun/src/advent-of-code-2023/day_03_input.txt"
lines = lines_to_arr(PATH)


def contain_symbol(arr):
    print(arr)
    for i in arr:
        if i == ".": continue
        try:
            int(i)
        except ValueError:
            return True

    return False


# rows by col
# number
# symybol

# 0-0, 0-1,
# 1-1, 1-2, 1-3, 1-4
# 2-1, 2-2, 2-3, 2-3
# 2-1, 2-2, 2-3, 3-3


# Symbol Window
# x, y
# -1,-1 : 0, -1 : + 1 , - 1
# -1, 0 : 0, 0  : +1 , 0
# -1, +1 : 0, +1  : +1 , +1


# symbol = False
# total = 0

# for y, line in enumerate(lines):
#     # need the number
#     if y == 8:
#         pass
#     num = ""
#     for x, char in enumerate(line):
#         if char == ".":
#             if num != "":
#                 start = x - (len(num)) - 1 if x - (len(num)) - 1 > 0 else 0
#                 # start = x - (len(num)) if x - (len(num)) > 0 else 0
#                 t = len(line)
#                 # something wrong with this line

#                 endp = x + 1 if x + 1 < len(line) - 1 else x

#                 # print(f"Start: {start}")
#                 # print(f"End: {endp}")
#                 # y -1 look
#                 counted = False
#                 if y > 0:
#                     # print("Check above")
#                     if contain_symbol(lines[y - 1][start:endp]): counted = True

#                 # y look
#                 if contain_symbol(lines[y][start:endp]): counted = True

#                 # y + 1 look
#                 if y + 1 < len(lines):
#                     # print("Check below")
#                     if contain_symbol(lines[y + 1][start:endp]): counted = True
                
#                 if counted: 
#                     print(f"Counted: {num} on row {y}")
#                     total = total + int(num)
                    
#                 if not counted:
#                     pass
#                     # print(f"Not counted {num} on row {y}")
                
#                 num = ""
#                 # symbol = False
                
#             continue

#         try:
#             int(char)
#             if len(num) > 5:
#                 print(num)
#             num = num + char
#             # print(f"Number: {char} is at x: {x} y: {y}")
#         except ValueError:
#             # print(f"Symbol: {char} is at x: {x} y: {y}")
#             # symbols.append({"x": x, "y": y})
            
#             continue
        
        
symbol = False
total = 0

for y, line in enumerate(lines):
    # need the number
    if y == 8:
        pass
    num = ""
    for x, char in enumerate(line):
        try:
            int(char)
            if len(num) > 5:
                print(num)
            num = num + char
            # print(f"Number: {char} is at x: {x} y: {y}")
        except ValueError:
            if num != "":
                t = x + 1
                start = x - (len(num)) - 1 if x - (len(num)) - 1 > 0 else 0
                # start = x - (len(num)) if x - (len(num)) > 0 else 0
                
                # something wrong with this line
                endp = x + 1 if x + 1 < len(line) - 1 else x

                print(f"counting {num}")
                print(f"Start: {start}")
                print(f"End: {endp}")
                # y -1 look
                counted = False
                if y > 0:
                    # print("Check above")
                    if contain_symbol(lines[y - 1][start:endp]): counted = True

                # y look
                if contain_symbol(lines[y][start:endp]): counted = True

                # y + 1 look
                if y + 1 < len(lines):
                    # print("Check below")
                    if contain_symbol(lines[y + 1][start:endp]): counted = True
                
                if counted: 
                    print(f"Counted: {num} on row {y}")
                    total = total + int(num)
                    
                if not counted:
                    pass
                    # print(f"Not counted {num} on row {y}")
                
                num = ""
            # print(f"Symbol: {char} is at x: {x} y: {y}")
            # symbols.append({"x": x, "y": y})
            
            # continue


# for num in numbers:
# print(num)

# need to keep track of number and end or start then offset when we check ?
# give each number a uniq id so we dont add it twice

# iterat through numbers that way a number is only added once

print(f"total: {total} should be 6990162 and 548403 is wrong")
