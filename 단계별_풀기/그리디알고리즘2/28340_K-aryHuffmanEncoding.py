from sys import stdin
input = lambda:stdin.readline().rstrip()

import heapq

def 

for _ in range(int(input())):
    n, k = map(int, input().split())

    pq = []
    for c in list(map(int, input().split())):heapq.heappush(pq, -c)