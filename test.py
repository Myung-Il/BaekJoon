import sys
input = lambda:sys.stdin.readline().strip()
v, e = map(int,input().split())     # 노드의 수와 간선의 수

g = [[]for _ in range(v+1)]         # 그래프
for _ in range(e):                  #
    a, b = map(int,input().split()) # 두 관계 노드 입력
    g[a].append(b)                  # 그래프 그리기

d = [-1] * (v+1)         # 거리?
stk = []                 # 스택
visit = [False] * (v+1) # 시작 스택인지 확인
id = 0                   # ?

def dfs(cur):          # 현재 노드를 받아옴
    global id          # ?
    id += 1            # ? 갱신
    d[cur] = id        # 거리?에 ?를 받음
    stk.append(cur)    # 스택에 현재 위치를 지정
    visit[cur] = True # 시작 스택 기록
    
    p = id        # 부모 노드에 현재 노드 거리? 기록
    for nx in g[cur]: # 현재 노드의 이웃 노드 받음
        if d[nx] == -1:p = min(p, dfs(nx)) # 거리?가 없다면 
        elif visit[nx]:p = min(p, d[nx])
        
    if p == d[cur]:
        s = []
        while 1:
            node = stk.pop()
            visit[node] = False
            s.append(node)
            if cur == node: break
        print(id, "==", s)
    return p

for idx in range(1, v+1):     # 노드 1번부터 시작
    if d[idx] == -1: dfs(idx) # 거리?가 시작조차 안했다면
print(d, id) 
'''
7 9
1 4
4 5
5 1
1 6
6 7
2 7
7 3
3 7
7 2
'''