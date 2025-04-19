from sys import stdin
import heapq as hq
input = lambda:stdin.readline().rstrip()

def fs(a, order, mod=10**9+7):    # a^order mod
    y = 1
    while order > 0:
        if order & 1  == 1:
            y = (a * y) % mod
        a = (a * a) % mod
        order = order >> 1
    return y

def topologySort(load):
    indegree = 1<<(k+1)
    graph = [[]for _ in range(k+1)]

    load = sorted(load, reverse=True)
    for a, b in load:
        if indegree&1<<b:continue
        graph[a].append(b)
        indegree = indegree|1<<b

    queue = [] # 큐
    for idx in range(0, k):
        if not indegree&1<<idx:
            hq.heappush(queue, idx)

    result, order = 0, k-1
    while queue:
        x = hq.heappop(queue) # 현재 위치
        result += (n-k)*fs(n, order)
        order -= 1
        if not graph[x]: continue
        for g in graph[x]:hq.heappush(queue, g)
    return result


n, k, p = map(int, input().split())
load = [tuple(map(int, input().split()))for _ in range(p)]
print(topologySort(load))