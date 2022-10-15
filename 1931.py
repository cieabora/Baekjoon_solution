import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(list(map(int, sys.stdin.readline().split())))

nums.sort()
nums.sort(key=lambda x: x[1])

last = 0
result = 0
done = True
i = 0
while done:
    done = False
    for j in range(i, n):
        if last <= nums[j][0]:
            last = nums[j][1]
            done = True
            i += 1
            result += 1
            break
        else:
            i += 1

print(result)