from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()

# 변수
n = int(input())                # 노드의 갯수
graph = [[]for _ in range(n+1)] # 노드들의 연결된 트리
depth = [0] * (n+1)             # 각 노드의 깊이
visit = [False] * (n+1)         # 트리에서 방문했는지 확인
tree = [[0]*18 for _ in range(n+1)] # 2진씩 거리에 무엇이 있는지 기록


# 함수
def dfs(x, deep):
    visit[x] = True # 방문 설정
    depth[x] = deep # 깊이 설정

    for elm in graph[x]:       # 자식으로 무엇을 가지고 있는지
        if visit[elm]:continue # 알아보고 이미 지나갔다면 넘어간다
        tree[elm][0] = x       # x를 부모 노드로 둔 elm
        dfs(elm, deep+1)       # elm을 부모로 두고 다시 탐색 시작

def find():
    dfs(1, 0) # 거리 1의 부모 노드와 자식 노드 관계 정의
    for deep in range(1, 18):     # 거리 설정 (dfs에서 2**0을 미리 찾아둠)(2, 4, 8, ..., 2**17까지)
        for elm in range(1, n+1): # 각 elm의 2**거리의 요소를 기록해준다
            tree[elm][deep] = tree[tree[elm][deep-1]][deep-1]
            # 점화식
            # 0   1 2 4
            # 1 | 0    옆 트리에서 7의 3번 째 부모 노드를 알고 싶다면
            # 2 | 1    7에서 2거리에 있는 노드를 먼저 찾아준다 = 3
            # 3 | 1    7에서 3거리에 있는 노드는 3에서 1거리에 있는 노드와 같다
            # 4 | 2 1  3에서 1거리에 있는 노드는 1이다
            # 5 | 2 1  이렇게 거리를 축약시킬 수 있다
            # 6 | 3 1
            # 7 | 6 3

def lca(a, b):
    if depth[a]>depth[b]:a, b = b, a     # b를 무조건 깊은 것으로 둘것이다
    for deep in range(17, -1, -1):       # b와 a의 깊이가 같아지도록 한다, 그래야 공동 부모 노드를 찾을 수 있으니까
        if depth[b]-depth[a] >= 2**deep: # 깊이에서 본 두 노드 사이의 거리는 0이 같은 깊이
            b = tree[b][deep]            # 거리 차가 존재한다면 둘 중 하나가 이미 부모 노드로써 되어 있다
    if a==b:return a

    for deep in range(17, -1, -1):
        if tree[a][deep] != tree[b][deep]:
            a = tree[a][deep]
            b = tree[b][deep]
    return tree[a][0]


#
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b) # 노드간의
    graph[b].append(a) # 관계 기록

find() # 부모 노드와 자식 노드 설정
m = int(input())
for _ in range(m):
    a, b = map(int,input().split())
    print(lca(a, b))