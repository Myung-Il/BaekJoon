from sys import stdin
import heapq as q
input = lambda:stdin.readline().rstrip()

n = int(input())
queue = []

for idx in range(n):
    for elm in list(map(int, input().split())):
        q.heappush(queue, elm)
        if idx>0:q.heappop(queue)

print(queue[0])