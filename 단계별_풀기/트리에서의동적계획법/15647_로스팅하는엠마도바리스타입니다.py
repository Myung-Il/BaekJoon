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
setrecursionlimit(10**7)
input = lambda:stdin.readline().strip()


class Node:
    def __init__(self, N):
        self.num = N
        self.edge = dict()
    
    def add(self, nxt, dist):
        self.edge[nxt] = [1, dist]


weight = 0
def dfsSetting(idx, wei, visit):
    global weight
    weight += wei

    if visit & (1<<idx):return 1
    visit |= (1<<idx)

    total = 1
    for nxt in tree[idx].edge:
        if visit & (1<<nxt):continue
        res = dfsSetting(nxt, wei+1, visit)
        tree[idx].edge[nxt][0] = res
        total += res

    return total

def dfsSolve(idx, res, visit):
    result[idx] = res

    visit |= (1<<idx)
    for nxt, (cnt, dist) in tree[idx].edge.items():
        if visit & (1<<nxt):continue
        dfsSolve(nxt, res + dist*(N-cnt*2), visit)


N = int(input())
tree = [Node(idx)for idx in range(N+1)]
total = {name:0 for name in tree[1].edge}
result = [0]*(N+1)

for _ in range(N-1):
    u, v, d = map(int,input().split())
    tree[u].add(v, d)
    tree[v].add(u, d)

dfsSetting(1, 0, 1<<(N+1))
dfsSolve(1, weight, 1<<(N+1))
for r in result[1:]:print(r)