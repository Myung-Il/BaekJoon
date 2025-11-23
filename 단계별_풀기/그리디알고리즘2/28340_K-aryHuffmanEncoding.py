from sys import stdin
input = lambda:stdin.readline().rstrip()

import heapq

for _ in range(int(input())):
    n, k = map(int, input().split())

    pq = []
    for c in list(map(int, input().split())):heapq.heappush(pq, -c)

    limit = 0 if n<k else n-k
    lvl = 1
    idx = 1
    res = 0
    for _ in range(n-1):
        if idx==limit:lvl, idx = lvl+1, 1
        res-=heapq.heappop(pq)*lvl
        print(f"lvl:{lvl}, idx:{idx}, lim:{limit} =", res)
        idx += 1
    
    print(f"lvl:{lvl}, idx:{idx}, lim:{limit} =", res)