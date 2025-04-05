from sys import stdin
input = lambda:stdin.readline().rstrip()


def solve(s, p): # 현재 값, 부모 값
    visit[s] = 1 # 방문 기록

    for elm in l[s]:       # 다음으로 넘어갈 수 있는 노드 확인
        if elm==p:continue # 부모노드로는 갈 수 없으니 패스, 물론 돌아갈 부모 노드가 있을 때
        if visit[elm]:return 0        # 방문한 적 있다면 싸이클이 되었다는 뜻이니, 싸이클이 되었다고 알림
        if not solve(elm, s):return 0 # 아직 끝까지 못가서 싸이클이 되었는지 알 수 없으니 더 들어감
    return 1                          # 싸이클이 만들어진 적 없이 말단 노드까지 갔을 때


case = 1
while 1:
    n, m = map(int,input().split())
    if n==0 and m==0:break
    l = [[]for _ in range(n+1)]
    visit = [0]*(n+1)
    for _ in range(m):
        a, b = map(int,input().split())
        l[a].append(b)
        l[b].append(a)

    cnt = 0
    for idx in range(1, n+1):
        if visit[idx]==0:     # 방문 확인
            if solve(idx, 0): # 싸이클 확인
                cnt+=1        # 싸이클이 아니라면 +1
            
    if cnt>1:print(f"Case {case}: A forest of {cnt} trees.")
    elif cnt:print(f"Case {case}: There is one tree.")
    else:    print(f"Case {case}: No trees.")
    case+=1