import sys
n = int(input())
met = []
num = dict()
num[1] = 0
num[0] = 0
num[-1] = 0

for _ in range(n):
    met.append(list(map(int ,sys.stdin.readline().split())))

visit = [[0] * n for i in range(n)]

for y in range(n):
    for x in range(n):
        if visit[y][x] == 1:
            continue
        tmp = x
        while tmp < n:
            if met[y][x] == met[y][tmp]: 
                tmp += 1
            else:
                break
        width = tmp - x
        tmp = y
        while tmp < n:
            if met[y][x] == met[tmp][y]:
                tmp += 1
            else:
                break
        height = tmp - y
        l = min(height, width)
        while True:
            for i in range(l):
                for j in range(l):
                    if met[y][x] != met[y + i][x + j]:
                        l -= 1
                        continue
            for i in range(l):
                for j in range(l):
                    visit[y + i][x + j] = 1
            num[met[y][x]] += 1
            break
print(num[-1])
print(num[0])
print(num[1])