import time
import os

os.system('cls' if os.name == 'nt' else 'clear')
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

lyrics =[
    ("I know I can treat you better", 0.08, 1.0),
    ("Than he can",0.09, 0.8),
    ("and any girl like you deserves",0.08,1.5),
    ("a gentelman",0.09,1.5),
    ("Tell me why are we wasting time on all your wasted crying?",0.05,0.6),
    ("when you should be with me instead",0.05,0.4),
    ("I know I can treat you better",0.08,1.5),
    ("",0.09,1.6),
    ("BETTER THAN HE CANNNN",0.08,1.5),
    ("",0.5,1.6)
]

for line, char_delay, line_delay in lyrics:
    if line == "":
        print()
        time.sleep(line_delay)
        continue

    if line == "BETTER THAN HE CANNNN":
        print(RED, end='', flush=True)
    else:
        print(BLUE, end='', flush=True)

    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)

    print(RESET, end='', flush=True)

    print()
    time.sleep(line_delay)