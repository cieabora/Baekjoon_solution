import sys
n = int(input())
met = []

for i in range(n):
    met.append(list(map(int, sys.stdin.readline().split())))

num = dict()
for i in range(2):
    num[i] = 0

def sol(ln, scale):
    done = False
    for i in range(scale):
        for j in range(scale):
            if ln[0][0] != ln[i][j]:
                done = True
    if done:
        if scale == 1:
            num[ln[0][0]] += 1
        else:
            for i in range(2):
                for j in range(2):
                    sol([[ln[y][x] for x in range(scale // 2 * j, scale // 2 * (j + 1))] for y in range(scale // 2 * i, scale // 2 * (i + 1))], scale // 2)
    else:
        num[ln[0][0]] += 1
sol(met, n)
for i in range(2):
    print(num[i])