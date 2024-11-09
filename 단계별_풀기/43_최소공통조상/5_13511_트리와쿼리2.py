from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()


n = int(input())
graph = [[]for _ in range(n+1)]
depth = [0] * (n+1)
visit = [False] * (n+1)
tree = [[0]*18 for _ in range(n+1)]
cost = [[0]*18 for _ in range(n+1)]


def dfs(x, deep):
    visit[x] = True
    depth[x] = deep

    for elm, pay in graph[x]:
        if visit[elm]:continue
        tree[elm][0] = x
        cost[elm][0] = pay
        dfs(elm, deep+1)

def find():
    dfs(1, 0)
    for deep in range(1, 18):
        for elm in range(1, n+1):
            tree[elm][deep] = tree[tree[elm][deep-1]][deep-1]
            cost[elm][deep] += cost[cost[elm][deep-1]][deep-1]

def lca(a, b, c=0):
    pay = 0
    alist = []
    blist = []

    for deep in range(17, -1, -1):
        if depth[a]-depth[b] >= 2**deep:
            pay += cost[a][deep]
            alist.append(a)
            a = tree[a][deep]
    for deep in range(17, -1, -1):
        if depth[b]-depth[a] >= 2**deep:
            pay += cost[b][deep]
            blist.append(b)
            b = tree[b][deep]
    if a==b:
        l = alist+[0]+sorted(blist, reverse=True)
        return pay, l[c]

    for deep in range(17, -1, -1):
        if tree[a][deep] != tree[b][deep]:
            pay += cost[a][deep]+cost[b][deep]
            alist.append(a)
            blist.append(b)
            a = tree[a][deep]
            b = tree[b][deep]
    alist.append(a)
    blist.append(b)
    l = alist+[0]+sorted(blist, reverse=True)
    return pay+cost[a][0]+cost[b][0], l[c]


for _ in range(n-1):
    a, b, c = map(int,input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

find()
m = int(input())
for _ in range(m):
    t, *l = map(int,input().split())
    if t==1:print(lca(l[0], l[1])[0])
    if t==2:print(lca(l[0], l[1], l[2])[1])