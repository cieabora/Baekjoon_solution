import sys
import heapq
from collections import deque

t = int(input())
for _ in range(t):
    heap = []
    i = int(input())
    for __ in range(i):
        o, n = sys.stdin.readline().split()
        n = int(n)
        if o == 'I':
            heap.append(n)
        else:
            heap.sort()
            if n == -1:
                heap = 
    if len(heap):
        print(heap[-1], heap[0])
    else:
        print("EMPTY")