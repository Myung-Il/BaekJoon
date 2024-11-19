from collections import defaultdict, deque
import sys
sys.setrecursionlimit(600000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
raw_cash = [0] + [int(input()) for _ in range(n)]

visit = [-1]*(n+1)
scc_finished = [-1]*(n+1)
count = 0
id = 0
stk = []

def scc(node) :
    global id, count
    visit[node] = ret = id
    id += 1
    stk.append(node)
    for nxt in graph[node] :
        if scc_finished[nxt] > -1 :continue
        if visit[nxt] == -1 :scc(nxt)
        visit[node] = min(visit[node], visit[nxt])
    if ret == visit[node] :
        while stk :
            n = stk.pop()
            scc_finished[n] = count
            if n == node :break
        count += 1

for i in range(1, n+1) :
    if scc_finished[i] == -1 :
        scc(i)

start, restaurant = map(int, input().split())
w = [0]*count
edge_list = [set() for _ in range(count)]
max_cash = [0]*count
finish = [False]*count
for r in list(map(int, input().split())) :
    finish[scc_finished[r]] = True
result = 0

for i in range(1, n+1) :
    _i = scc_finished[i]
    w[_i] += raw_cash[i]
    for j in graph[i] :
        if _i != scc_finished[j] :
            edge_list[_i].add(scc_finished[j])
    if i == start : s = _i

def bfs(node) :
    max_cash[node] = w[node]
    q = deque([node])
    while q :
        n = q.popleft()
        for nxt in edge_list[n] :
            if max_cash[nxt] < max_cash[n] + w[nxt] :
                max_cash[nxt] = max_cash[n] + w[nxt]
                q.append(nxt)

bfs(s)
for i in range(count) :
    if finish[i] :
        result = max(result, max_cash[i])
print(result)
print(max_cash)