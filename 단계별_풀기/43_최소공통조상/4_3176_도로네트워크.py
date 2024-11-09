from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()

# 변수
n = int(input())
graph = [[]for _ in range(n+1)]
depth = [0] * (n+1)
visit = [False] * (n+1)
tree = [[0]*18 for _ in range(n+1)]
mntree = [[float('inf')]*18 for _ in range(n+1)]
mxtree = [[0]*18 for _ in range(n+1)]


# 함수
def dfs(x, deep):
    visit[x] = True
    depth[x] = deep

    for elm, pay in graph[x]:
        if visit[elm]:continue
        tree[elm][0] = x
        mntree[elm][0] = pay
        mxtree[elm][0] = pay
        dfs(elm, deep+1)

def find():
    dfs(1, 0)
    for deep in range(1, 18):
        for elm in range(1, n+1):
            tree[elm][deep] = tree[tree[elm][deep-1]][deep-1]
            mntree[elm][deep] = min(mntree[tree[elm][deep-1]][deep-1], mntree[elm][deep-1])
            mxtree[elm][deep] = max(mxtree[tree[elm][deep-1]][deep-1], mxtree[elm][deep-1])

def lca(a, b):
    if depth[a]>depth[b]:a, b = b, a
    mn = float('inf')
    mx = 0

    for deep in range(17, -1, -1):
        if depth[b]-depth[a] >= 2**deep:
            mn = min(mn, mntree[b][deep])
            mx = max(mx, mxtree[b][deep])
            b = tree[b][deep]
    if a==b:return mn, mx

    for deep in range(17, -1, -1):
        if tree[a][deep] != tree[b][deep]:
            mn = min(mn, mntree[a][deep], mntree[b][deep])
            mx = max(mx, mxtree[a][deep], mxtree[b][deep])
            a = tree[a][deep]
            b = tree[b][deep]
    mn = min(mn, mntree[a][0], mntree[b][0])
    mx = max(mx, mxtree[a][0], mxtree[b][0])
    return mn, mx


#
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

find()
m = int(input())
for _ in range(m):
    a, b = map(int,input().split())
    print(*lca(a, b))