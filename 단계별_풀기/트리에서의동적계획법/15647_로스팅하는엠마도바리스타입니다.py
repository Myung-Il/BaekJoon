'''
N개의 정점을 가진 트리 형태의 농장 연결 시스템
N : 1~N
u, v : 서로 연결되어 있음
d : 거리

결과 : 각 특정 농장에서 다른 농장까지의 거리 합을 구해야 함

10
1 2 1
2 3 1
2 4 1
4 7 1
4 8 1
4 5 1
1 6 1
6 9 1
6 10 1
'''

from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10**7)
input = lambda:stdin.readline().strip()

def BFS(start):
    q = deque([start])
    visit = 1<<N+1

    while q:
        node = q.popleft()
        
        visit |= 1<<node
        for nxt, d in tree[node]:
            if visit & 1<<nxt: continue
            q.append(nxt)

            parent[nxt] = node
            child[node].append(nxt)
            dist[nxt] = d

def DFS(start):
    for nxt in child[start]:
        DFS(nxt)
        cnt[start] += cnt[nxt]
        res[start] += res[nxt] + dist[nxt]*cnt[nxt]
    
def solve(start):
    res[nxt] = res[start] + dist[nxt]*(N - cnt[nxt]*2)
    for nxt in child[start]:solve(nxt)


N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, d = map(int,input().split())
    tree[u].append([v, d])
    tree[v].append([u, d])

parent = [0]*(N+1)
child = [[] for _ in range(N+1)]
dist = [0]*(N+1)

cnt = [1]*(N+1)
res = [0]*(N+1)

BFS(1)
DFS(1)
solve(1)

print(*res[1:], sep="\n")