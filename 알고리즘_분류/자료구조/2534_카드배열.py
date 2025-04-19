from sys import stdin
import heapq as hq
input = lambda:stdin.readline().rstrip()

def topologySort(load):
    indegree = 1<<(k+1)
    graph = [[]for _ in range(k+1)]

    load = sorted(load, reverse=True)
    for a, b in load:
        if indegree&1<<b:continue
        graph[a].append(b)
        indegree = indegree|1<<b

    result = []
    queue = [] # 큐
    for idx in range(0, k):
        if not indegree&1<<idx:
            hq.heappush(queue, idx)

    while queue:
        x = hq.heappop(queue) # 현재 위치
        result.append(x)
        if not graph[x]: continue
        for g in graph[x]:hq.heappush(queue, g)
    return result

def fs(a, x, n):    # a^x mod n
    y = 1
    while x > 0:
        if x & 1  == 1:         # 지수의 LSB가 1인지 확인
            y = (a * y) % n     # Multiply Operation
        a = (a * a) % n         # Square Operation
        x = x >> 1
    return y

def solve(group, diff=0, mod=10**9+7):
    result = 0
    order = k-1
    for elm in group:
        result += (elm+diff)*fs(n, order, mod)
        order -= 1
    return result


n, k, p = map(int, input().split())
load = [tuple(map(int, input().split()))for _ in range(p)]
group = topologySort(load)

mn = solve(group)
mx = solve(group, n-k)

print(mx-mn)