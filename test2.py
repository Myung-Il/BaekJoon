from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10**7)
input = lambda:stdin.readline().strip()

def BFS(start):
    q = deque([start])

    while q:
        node = q.popleft()
        
        for nxt, d in tree[node]:
            if child[nxt]: continue
            q.append(nxt)

            parent[nxt] = node
            child[node].append(nxt)
            dist[nxt] = d
            print(node, "->", nxt, child, dist)

def DFS(start):
    for nxt in child[start]:
        DFS(nxt)
        cnt[start] += cnt[nxt]
        res[start] += res[nxt] + dist[nxt]*cnt[nxt]
    
def solve(start):
    res[start] = res[parent[start]] + dist[start]*(N - cnt[start]*2)
    for nxt in child[start]:solve(nxt)


N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, d = map(int,input().split())
    tree[u].append([v, d])
    tree[v].append([u, d])

parent = [1]*(N+1)
child = [[] for _ in range(N+1)]
dist = [0]*(N+1)

cnt = [1]*(N+1)
res = [0]*(N+1)

BFS(1)
DFS(1)
solve(1)

print(*res[1:], sep="\n")