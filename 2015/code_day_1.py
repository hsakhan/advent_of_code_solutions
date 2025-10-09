import time
import random
import itertools

# ----------------------------------------------------------------
# You can find all decorators and stuff in folder named ...
# I have just add it here so u can copypaste solution and test it
# without importing repo.

# Viel Spass!
# ----------------------------------------------------------------

# Simple decorator to calculate functions execution time.
def exec_time(func):
    def wrapper(*args, **kwargs):
        start: float = time.time()
        ret = func(*args, **kwargs)
        end: float = time.time()
        diff: float = round(end - start, 6)
        return (ret, diff)
    return wrapper


# Function to generate random input.
@exec_time
def generate_input(*, file: str, 
                   lines: int, 
                   max_len: int) -> int:
    
    with open(file, "w") as file:
        _alphabet: str = "()"
        for _ in itertools.repeat(0, lines):
            str_len: int = random.randint(1, max_len)
            tmp: str = ""
            for _ in itertools.repeat(0, str_len):
                tmp += _alphabet[random.randint(0, 1)]
            _txt = tmp + "\n"
            file.write(_txt)
    return 0

# Part 1 (a).

# Default simple solution, first that came to my mind
@exec_time
def deliver_quest_a(route: str) -> int:
    floor: int = 0
    for direction in route:
        if direction == '(':
            floor += 1
        else:
            floor -= 1
    return floor


# Looks cleaner (meiner Meinung nach) and little bit faster 
@exec_time
def deliver_quest_aa(route: str) -> int:
    floor: int = 0
    _directions: dict[str, int] = {'(': 1, ')': -1}
    for direction in route:
        floor += _directions[direction]
    return floor


# One line solution, looks great but idk. I would rather do not use this one in real projects.
# Just wanna show you guys that it is possible.
@exec_time
def deliver_quest_aaa(route: str) -> int:
    return sum([1 if i == '(' else -1 for i in route])


# Cleanest and fastest solution. Love it
@exec_time
def deliver_quest_aaaa(route: str) -> int:
    return route.count('(') - route.count(')')


# Part 2 (b).

# First that came to my mind, just go through. By finding -1 break.
@exec_time
def deliver_quest_b(user_input: str) -> int:
    floor: int = 0
    steps: int = 0
    _directions: dict[str, int] = {'(': 1, ')': -1}
    for direction in user_input:
        floor += _directions[direction]
        steps += 1
        if floor < 0:
            break
    return steps


# No need to have extra counter, enum helps.
@exec_time
def deliver_quest_bb(user_input: str) -> int:
    floor: int = 0
    _directions: dict[str, int] = {'(': 1, ')': -1}
    ret: int = 0
    for step, direction in enumerate(user_input, 1):
        floor += _directions[direction]
        if floor < 0:
            ret = step
            break
    return ret


# AI solution. Actually GPT wrote it with return instead of break but i do not like this way.
# (Geschmacksache)
@exec_time
def deliver_quest_bbb(user_input: str) -> int:
    floor: int = 0
    ret: int = 0
    for i, ch in enumerate(user_input, start=1):
        floor += 1 if ch == '(' else -1
        if floor < 0:
            ret = i
            break
    return ret


# TEST YOURSELF

_input: str | None = None

path_to_my_file: str = "./2015/day1/input_day_1.txt"           # file where u want to save your test input
lines_to_generate: int  = 10_000                               # how many lines will take ur file
line_max_length: int = 1_000                                   # how many symbols will take one line 

with open(path_to_my_file, "r") as file:
    _input = file.read()

if _input == "":
    ret, call_time = generate_input(file=path_to_my_file,
                                    lines=lines_to_generate,
                                    max_len=line_max_length)

print("Start:")
print(f"{path_to_my_file=}")

summ1, summ2, summ3, summ4, summ5, summ6, summ7 = 0, 0, 0, 0, 0, 0, 0
for _ in _input.splitlines():

    ret, call_time = deliver_quest_a(_)
    summ1 += call_time
    
    ret, call_time = deliver_quest_aa(_)
    summ2 += call_time
    
    ret, call_time = deliver_quest_aaa(_)
    summ3 += call_time
    
    ret, call_time = deliver_quest_aaaa(_)
    summ4 += call_time

    ret, call_time = deliver_quest_b(_)
    summ5 += call_time
    
    ret, call_time = deliver_quest_bb(_)
    summ6 += call_time
    
    ret, call_time = deliver_quest_bbb(_)
    summ7 += call_time

print("Part 1.")
print("deliver_quest_a: ", summ1)
print("deliver_quest_aa: ", summ2)
print("deliver_quest_aaa: ", summ3)
print("deliver_quest_aaaa: ", summ4)

print("Part 2.")
print("deliver_quest_b: ", summ5)
print("deliver_quest_bb: ", summ6)
print("deliver_quest_bbb: ", summ7)