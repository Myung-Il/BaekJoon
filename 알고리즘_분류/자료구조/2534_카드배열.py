from sys import stdin
import heapq as hq
input = lambda:stdin.readline().rstrip()

def topologySort(load):
    # 위상 정렬렬
    indegree = [0]*(k+1) # 부모 수
    graph = [[]for _ in range(k+1)]

    load = sorted(load, reverse=True)
    for a, b in load:
        if indegree[b]:continue
        graph[a].append(b)
        indegree[b] += 1

    result = []
    queue = [] # 큐
    for idx in range(0, k):
        if not indegree[idx]:
            hq.heappush(queue, idx)
    
    print(indegree)
    print(graph)
    print(queue)

    while queue:
        x = hq.heappop(queue) # 현재 위치
        result.append(x)
        if not graph[x]: continue
        for g in graph[x]:hq.heappush(queue, g)
    return result

def solve(group, diff=0):
    result = 0
    order = k-1
    for elm in group:
        result += (elm+diff)*n**order
        order -= 1
    return result


n, k, p = map(int, input().split())
load = [tuple(map(int, input().split()))for _ in range(p)]
group = topologySort(load)

mn = solve(group)
mx = solve(group, n-k)

print(mn, mx)
print(mx-mn)