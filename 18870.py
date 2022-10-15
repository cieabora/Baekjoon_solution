import heapq
import sys

def heapsort(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, value)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
nums = list(set(x))
nums = heapsort(nums)
for i in x:
    l = 0
    r = len(nums)
    while l <= r:
        m = (l + r) // 2
        if nums[m] < i:
            l = m + 1
        elif nums[m] > i:
            r = m - 1
        elif nums[m] == i:
            print(m, end=" ")
            break
print()