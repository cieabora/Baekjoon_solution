import sys
a, b = map(int, sys.stdin.readline().split())
first = (a + b) / 2
second = a - first
if first % 1 != 0:
    print(-1)
elif first < 0 or second < 0:
    print(-1)
else:
    print(max(int(first), int(second)), min(int(first), int(second)))
