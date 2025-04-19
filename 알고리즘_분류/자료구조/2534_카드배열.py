from sys import stdin
import heapq as hq
from collections import deque
input = lambda:stdin.readline().rstrip()

def topologySort(type, range):
    # 위상 정렬렬
    indegree = [0]*(k+1) # 부모 수
    graph = dict()       # 진입

    for a, b in load:
        if graph.get(a):hq.heappush(graph[a], b*type)
        else:
            graph[a] = []
            hq.heappush(graph[a], b*type)
        indegree[b] += 1

    result = []     # 결과값
    queue = deque() # 큐
    s = set()
    for idx in range:
        if not indegree[idx] and idx not in s:
            group = []
            queue.append(idx)
            while queue:
                x = queue.popleft() # 현재 위치
                s.add(x)
                group.append(x)     # 위치 추가
                if not graph.get(x): continue
                for g in graph[x]:
                    node = g*type
                    indegree[node] -= 1    # 차수 감소
                    if indegree[node]==0:  # 더 이상 연결된 부모가 없다면,
                        queue.append(node) # 스스로 들고 일어남
            result.append(group)
    return result

def solve(list, diff=0):
    result = 0
    order = k-1
    for group in list:
        for elm in group:
            result += (elm+diff)*n**order
            order -= 1
    return result

n, k, p = map(int, input().split())
load = [list(map(int, input().split()))for _ in range(p)]

mn = solve(topologySort(1, range(0, k)))
mx = solve(topologySort(-1, range(k-1, -1, -1)), n-k)
print(mx-mn)