import sys
n = int(input())
ln = []

for i in range(n):
    ln.append(list(map(int, sys.stdin.readline().split())))

num = dict()
for i in range(-1, 2):
    num[i] = 0

def sol(scale, x_start, y_start):
    done = False
    start = ln[y_start][x_start]
    for y in range(scale):
        for x in range(scale):
            if start != ln[y_start + y][x_start + x]:
                done = True
                break
        if done:
            break

    if done:
        if scale == 1:
            num[ln[x_start][y_start]] += 1
        else:
            next_scale = scale//3
            for i in range(3):
                for j in range(3):
                    sol(next_scale, x_start + next_scale * i, y_start + next_scale * j)
    else:
        num[ln[y_start][x_start]] += 1
sol(n, 0, 0)
for i in range(-1, 2):
    print(num[i])