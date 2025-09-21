from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()


def scc(cur):
    global id
    id += 1
    visit[cur] = id
    stk.append(cur)

    check = id
    for nx in graph[cur]:
        if not visit[nx]:check = min(check, scc(nx))
        if visit[nx]:
            check = min(check, visit[nx])
            v[nx] -= 1
    
    if check==visit[cur]:
        part = []
        groupV.append(0)
        while True:
            node = stk.pop()
            part.append(node)
            visit[node] = n
            groupV[-1] += v[node]
            if node==cur:break
        groupN.append(sorted(part))
    return check


k = int(input())
for flag in range(k):
    if flag:input()
    n, m = map(int,input().split())
    graph = [[]for _ in range(n)]
    v = [0] * n
    for _ in range(m):
        a, b = map(int,input().split())
        graph[a].append(b)
        v[b] += 1

    id = 0
    visit = [0] * n
    stk = []
    groupN = []
    groupV = []
    
    for elm in range(n):
        if not visit[elm]:scc(elm)
    
    cnt = 0
    result = []
    for idx in range(len(groupV)):                    # 모든 그룹이 연결되어 있어야 하기때문에
        if groupV[idx]==0:                            # 마지막에만 0이면 된다
            for elm in groupN[idx]:result.append(elm) # 
            cnt += 1

    if cnt == 1:print(*result, sep='\n')
    else:print("Confused")
    print()