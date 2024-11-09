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
            if tree[elm][deep]:
                cost[elm][deep] = cost[tree[elm][deep-1]][deep-1] + cost[elm][deep-1]

def lca(a, b):
    if depth[a]>depth[b]:a, b = b, a

    for deep in range(18):
        if (depth[b]-depth[a])&1<<deep:
            b = tree[b][deep]
    if a==b: return a

    for deep in range(17, -1, -1):
        if tree[a][deep] != tree[b][deep]:
            a = tree[a][deep]
            b = tree[b][deep]
    return tree[a][0]



for _ in range(n-1):
    a, b, c = map(int,input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

find()
m = int(input())
for _ in range(m):
    t, *l = map(int,input().split()) # 입력
    a, b = l[0], l[1]                # 숫자 2개 변수 지정
    lvl = depth[lca(a, b)]           # 공통 부모 노드의 깊이 설정
    if t==1:                                        # 1번 일 때
        s, adp, bdp = 0, depth[a]-lvl, depth[b]-lvl # 합, 깊이 간의 거리
        for deep in range(18):     # 예제 1을 기준으로
            if adp & 1<<deep:      # adp가 2면 10
                s += cost[a][deep] # s += cost[4][2] >>> 2
                a = tree[a][deep]  # a = tree[4][2]  >>> 1

            if bdp & 1<<deep:
                s += cost[b][deep] # >>> 3
                b = tree[b][deep]  # >>> 1
        print(s) # >>> 5
    else:
        c = l[2] # a ~ b 사이에 노드 중 c번째는 무엇인가
        if c<=depth[a]-lvl:           # a에서부터 c번째 <= a깊이 -공통 부모 노드의 깊이 +1
            for deep in range(18):    # c(3) <= a(2)-lvl(0)+1 == 3
                if c-1 & 1<<deep:     # 4>> 2>> 1 <<3 <<6
                    a = tree[a][deep]
            print(a)
        else:
            c = depth[a]+depth[b]-c-2*lvl +1 # c번째 = a깊이+b깊이 -c번째-공통의 깊이*2 +1
            for deep in range(18):           # c = a(2)+b(2) -c(4)-lvl(0)*2 +1 == 1
                if c & 1<<deep:              # c = 1 >>> 1
                    b = tree[b][deep]        # 6>>> 3
            print(b)