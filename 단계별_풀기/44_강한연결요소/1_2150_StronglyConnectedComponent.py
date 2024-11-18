from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()


def scc(cur):         # 현재 그룹을 만드려는 숫자
    global id         # 고유 번호
    id += 1           # 새로운 고유 번호를 받음
    scanId[cur] = id  # 일단 내가 시작이니, 시작노드의 고유 번호는 본인
    visit[cur] = 1    # 방문 확인
    stack.append(cur) # 스택

    check = id                                        # 고유 번호 기록
    for nx in graph[cur]:                             # 그룹을 만들기 위해서 이어진 다른 노드 탐색
        if not scanId[nx]:check = min(check, scc(nx)) # 다음 노드의 고유 번호가 없다면, 고유번호를 만들러감->
        elif visit[nx]:check = min(check, scanId[nx]) # 방문한 적있다면(고유번호는 있다는 이야기), 숫자가 작을수록 그룹의 시작에 가깝다
        # 고유 번호를 만들러 간다고 했지만 그룹으로 쓸 노드가 더 있는지 확인하는 역할도 한다
        # min을 쓰는 이유는 id의 값이 작을수록 시작노드에 가깝기 때문에 시작으로 돌아가기 위해서는 min을 써야한다

    if check == scanId[cur]:          # 한 시작으로 돌아왔다면
        reserve = []                  # 일부 그룹을 저장할 리스트
        while True:                   # 반복
            node = stack.pop()        # 스택에서 꺼내고
            visit[node] = 0           # 방문처리
            reserve.append(node)      # 일부 그룹에 집어 넣는다
            if cur == node:break      # 꺼낸게 시작이라면 멈춘다
        group.append(sorted(reserve)) # 그리고 정렬 후 그룹에 저장한다
    return check # 시작이 아닐 경우 자신의 고유 번호를 반환한다
                 # 그래야 시작 id를 찾았을 때 줄 수 있다


v, e = map(int,input().split())     # 노드의 수, 간선의 수
graph = [[]for _ in range(v+1)]     # 그래프
for _ in range(e):                  # 입력
    a, b = map(int,input().split()) # a -> b
    graph[a].append(b)

scanId = [0] * (v+1)  # 그룹의 시작노드를 기록하는 곳
visit = [0] * (v+1)   # 방문 기록
stack = []            # 스택
id = 0                # 고유 번호

group = []                      # 그룹
for idx in range(1, v+1):       # 노드 조회
    if not scanId[idx]:scc(idx) # 노드를 방문한 적 없다면 그룹을 만들러 감
group = sorted(group)           # 그룹 정렬

print(len(group))
for elm in group:print(*elm, -1)