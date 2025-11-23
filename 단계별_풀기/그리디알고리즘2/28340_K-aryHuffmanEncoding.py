from sys import stdin
input = lambda:stdin.readline().rstrip()

import heapq

for _ in range(int(input())):
    n, k = map(int, input().split())

    pq = []
    for c in list(map(int, input().split())):heapq.heappush(pq, -c)

    limit = k-1
    lvl = 1
    idx = 0
    res = 0
    for _ in range(n-1):
        if idx==limit:lvl, idx = lvl+1, 0
        res-=heapq.heappop(pq)*lvl
        idx += 1
    res-=heapq.heappop(pq)*lvl
    
    print(res)