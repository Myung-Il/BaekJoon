from sys import stdin
import heapq as q
input = lambda:stdin.readline().rstrip()

n = int(input())
queue = []

for _ in range(n):
    for elm in input().split():
        q.heappush(queue, -int(elm))

for _ in range(n):
    result = q.heappop(queue)

print(-result)