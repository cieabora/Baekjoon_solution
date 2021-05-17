import sys
for case in range(3):
    n = int(sys.stdin.readline())
    res = 0
    for case2 in range(n):
        res += int(sys.stdin.readline())
    if res > 0: print("+")
    elif res < 0: print("-")
    else: print(0)