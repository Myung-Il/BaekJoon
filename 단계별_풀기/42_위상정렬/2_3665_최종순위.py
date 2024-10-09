from collections import deque
from sys import stdin
input=lambda:stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    t = int(input())
    ti = list(map(int,input().split()))

    m = int(input())
    l = {}
    v = [0]*(t+1)
    for idx in range(t):
        l[ti[idx]] = ti[idx+1:] # 옛날 우승팀 다음으로 오는 팀을 순서대로 저장
        v[ti[idx]] = idx        # 옛날 팀들의 순서를 기록, 0 1 2 3 ...
    
    for _ in range(m):
        a, b = map(int,input().split())
        if a in l[b]:a, b = b, a # 순서상 b가 먼저온다면 a, b를 바꿔줌
        l[a].remove(b) # 먼저 오는 것에서 다음에 오는 것을 제거
        l[b].append(a) # 다음에 오는 팀 다음으로 먼저 오는 팀으로 설정, 그냥 순서 바꾼거
        v[a] += 1      # 순서가 밀려났으니 +1
        v[b] -= 1      # 순서가 당겨졌으니 -1


    q = deque([elm for elm in ti if not v[elm]])
    # 0을 찾을거임, 이게 첫번째로 출력될 얘임

    result = []
    while q: # 팀이 순환을 이루면 0이 없으니 알아서 q가 비게 됨
        x = q.popleft()
        result.append(x)
        for elm in l[x]:
            v[elm] -= 1
            if not v[elm]:q.append(elm)
            
    if len(result)!=t:print("IMPOSSIBLE") # 문제가 있을 때
    else:             print(*result)      # 없을 때