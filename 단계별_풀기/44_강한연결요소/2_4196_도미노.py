from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()


def scc(cur):
    global id
    id += 1
    pwd[cur] = id
    stack.append(cur)
    visit[cur] = True

    p = id
    for elm in graph[cur]:
        if not pwd[elm]:p = min(p, scc(elm))
        if visit[elm]:
            p = min(p, pwd[elm])
            v[elm] -= 1 # 지나간 간선은 없앤다
    
    if p==pwd[cur]:
        s = []; group.append(0)
        while True:
            node = stack.pop()
            s.append(node)
            visit[node] = False
            group[-1] += v[node] # 최종적으로 그룹에 저장되는 숫자가 0이나 1이다
                                 # 0일 경우는 어딘가에서 시작에서 해당 그룹으로 들어오는 간선이 없다는 이야기이다
                                 # 1일 경우는 어딘가에서 시작에서 해당 그룹으로 들어오는 간선이 있다는 이야기이다
                                 # 예시 [1]-> [2-> 3-> 4-> 2]
                                 #         노드 1 2 3 4 (2만 들어오는 간선이 2개인 이유는
                                 # 오는 간선 수 0 2 1 1   1과 4에서 하나씩 받기 때문이다)
                                 # 4는 2가 이미 방문 되어 있기 때문에 2와의 간선을 하나 없앤다
                                 # 이후 3은 4를 방문 했기 때문에 4와의 간선을 하나 없앤다, 2까지 반복
                                 # p==pwd[2]일 때
                                 #         노드 1 2 3 4
                                 # 오는 간선 수 0 1 0 0
                                 # 위와 같은 경우로 변한다, 허나 아직 2에 들어오는 간선이 남아 있으니
                                 # 그룹은 만들어졌지만 도미노는 아직 연결되어 있다는 이야기가 된다
            if cur==node:break
    return p


k = int(input())
for _ in range(k):
    n, m = map(int,input().split())
    graph = [[]for _ in range(n+1)] # 그래프
    pwd = [0] * (n+1)               # 조상노드 id 기록
    stack = []                      # 스택
    visit = [False] * (n+1)         # 방문
    group = []                      # 그룹
    v = [0] * (n+1)                 # 오는 간선의 정보
    id = 0                          #

    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        v[b] += 1          # b로 오는 간선의 수 +1
    
    for idx in range(1, n+1):
        if not pwd[idx]:scc(idx)
    print(group.count(0))