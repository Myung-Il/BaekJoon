from sys import stdin
from collections import deque
input = lambda:stdin.readline().rstrip()

def topologySort(load, bool, diff=0):
    # 위상 정렬렬
    indegree = [0]*(k+1) # 부모 수
    graph = dict()       # 진입

    load = sorted(load, reverse=bool)
    for a, b in load:
        if graph.get(a):graph[a].append(b)
        else: graph[a] = [b]
        indegree[b] += 1

    result = 0
    order = k-1
    queue = deque() # 큐
    for idx in sorted(range(0, k), reverse=bool):
        if not indegree[idx]:
            queue.append(idx)
            while queue:
                x = queue.popleft() # 현재 위치
                result += (x+diff)*n**order
                order -= 1
                if not graph.get(x): continue
                for g in graph[x]:
                    node = g
                    indegree[node] -= 1    # 차수 감소
                    if indegree[node]==0:  # 더 이상 연결된 부모가 없다면,
                        queue.append(node) # 스스로 들고 일어남
                        indegree[node] -= 1
                
    return result

n, k, p = map(int, input().split())
load = [tuple(map(int, input().split()))for _ in range(p)]

mn = topologySort(load, False)
mx = topologySort(load, True, n-k)
print(mx-mn)