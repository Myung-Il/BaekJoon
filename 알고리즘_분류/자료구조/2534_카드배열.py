from sys import stdin
import heapq as hq
input = lambda:stdin.readline().rstrip()

def topologySort(load):
    # 위상 정렬렬
    indegree = [0]*(k+1) # 부모 수
    graph = [[]for _ in range(k+1)]

    load = sorted(load)
    for a, b in load:
        graph[a].append(b)
        indegree[b] += 1

    result = []
    queue = [] # 큐
    for idx in range(0, k):
        if not indegree[idx]:
            hq.heappush(queue, idx)

    while queue:
        x = hq.heappop(queue) # 현재 위치
        result.append(x)
        if not graph[x]: continue
        for g in graph[x]:
            node = g
            indegree[node] -= 1    # 차수 감소
            if indegree[node]==0:  # 더 이상 연결된 부모가 없다면,
                hq.heappush(queue, node) # 스스로 들고 일어남
                indegree[node] -= 1
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

print(mx-mn)