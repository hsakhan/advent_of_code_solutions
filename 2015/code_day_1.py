import time
import random
import itertools
import pathlib
from rich import print as rprint

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
def generate_input(*, file, 
                   lines: int, 
                   max_len: int) -> int:
    
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

rprint("[bold green]-Advent-Of-Code-2015-Day-1-")

file_path = pathlib.Path("./2015/day1/input_day_1.txt")        # file where u want to save your test input
lines_to_generate: int  = 10_000                               # how many lines will take ur file
line_max_length: int = 1_000                                   # how many symbols will take one line 

_input: str | None = None

if not file_path.exists():
    with open(file_path, "w+") as file:
        generate_input(file=file,
                       lines=lines_to_generate,
                       max_len=line_max_length)
        rprint(f"[bold green]Test input file was created. (path: {file_path})")
        file.seek(0)
        _input = file.read()
        rprint("[bold blue]Reading test input file.")
else:
    with open(file_path, "r") as file:
        _input = file.read()
        rprint("[bold blue]Reading test input file.")

rprint(f"[bold blue]Starting tests.")

_test_1: dict[function, float] = {
    "deliver_quest_a": 0.0,
    "deliver_quest_aa": 0.0,
    "deliver_quest_aaa": 0.0,
    "deliver_quest_aaaa": 0.0,
}

_test_2: dict[function, float] = {
    "deliver_quest_b": 0.0,
    "deliver_quest_bb": 0.0,
    "deliver_quest_bbb": 0.0,
}

for _ in _input.splitlines():

    ret, call_time = deliver_quest_a(_)
    _test_1["deliver_quest_a"] += call_time
    
    ret, call_time = deliver_quest_aa(_)
    _test_1["deliver_quest_aa"] += call_time
    
    ret, call_time = deliver_quest_aaa(_)
    _test_1["deliver_quest_aaa"] += call_time
    
    ret, call_time = deliver_quest_aaaa(_)
    _test_1["deliver_quest_aaaa"] += call_time

    ret, call_time = deliver_quest_b(_)
    _test_2["deliver_quest_b"] += call_time
    
    ret, call_time = deliver_quest_bb(_)
    _test_2["deliver_quest_bb"] += call_time
    
    ret, call_time = deliver_quest_bbb(_)
    _test_2["deliver_quest_bbb"] += call_time

rprint("[bold red]-Part 1.-")
print("deliver_quest_a - time:", _test_1["deliver_quest_a"])
print("deliver_quest_aa - time:", _test_1["deliver_quest_aa"])
print("deliver_quest_aaa - time:", _test_1["deliver_quest_aaa"])
print("deliver_quest_aaaa - time:", _test_1["deliver_quest_aaaa"])
rprint(f"[bold yellow]Best time: {min(_test_1.values())}")

rprint("[bold red]-Part 2.-")
print("deliver_quest_b - time:", _test_2["deliver_quest_b"])
print("deliver_quest_bb - time:", _test_2["deliver_quest_bb"])
print("deliver_quest_bbb - time:", _test_2["deliver_quest_bbb"])
rprint(f"[bold yellow]Best time: {min(_test_2.values())}")
