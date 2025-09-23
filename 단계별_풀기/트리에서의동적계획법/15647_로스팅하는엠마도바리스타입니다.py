'''
N개의 정점을 가진 트리 형태의 농장 연결 시스템
N : 1~N
u, v : 서로 연결되어 있음
d : 거리

결과 : 각 특정 농장에서 다른 농장까지의 거리 합을 구해야 함
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)
input = lambda:stdin.readline().strip()


class Node:
    def __init__(self, N):
        self.num = N
        self.edge = dict()
    
    def add(self, nxt, dist):
        self.edge[nxt] = dist


def path(idx, acnt, visit):
    res = acnt

    visit |= (1<<idx)
    for k, v in tree[idx].edge.items():
        if visit&(1<<k): continue
        res += path(k, acnt+v, visit)
    return res


N = int(input())
tree = [Node(idx)for idx in range(N+1)]

for _ in range(N-1):
    u, v, d = map(int,input().split())
    tree[u].add(v, d)
    tree[v].add(u, d)

print(*[path(i, 0, 1<<(N+1))for i in range(1, N+1)], sep='\n')