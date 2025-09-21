from sys import stdin
import heapq
input = lambda:stdin.readline().rstrip()

def dijkstra(start, end):
    tree = [float("inf")]*(n+1)
    track = [[start]for _ in range(n+1)]
    tree[start] = 0
    h = [[0, start]]
    while h:
        cost, point = heapq.heappop(h)
        if tree[point]<cost:continue
        for e, c in bus[point]:
            path = cost + c
            if path < tree[e]:
                tree[e] = path
                heapq.heappush(h, [path, e])
                track[e] = track[point] + [e]
    return tree[end], track[end]

n = int(input())
m = int(input())
bus = [[]for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int,input().split())
    bus[s].append([e, c])
start, end = map(int,input().split())
cnt, ans = dijkstra(start, end)
print(cnt)
print(len(ans))
print(*ans)