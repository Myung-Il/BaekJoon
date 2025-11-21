from sys import stdin
input = lambda:stdin.readline().strip()

from collections import deque

n, m, c, d = map(int, input().split())
hit = list(map(int, input().split()))
dp = [[0]*(m+1)for _ in range(n)]

def taste(i, t):return m-abs(hit[i]-t)

for t in range(1, m+1):dp[0][t] = taste(0, t)
for i in range(1, n):
    # 필요한 부분만 보기
    for k in range(1, c+1):
        # 슬라이딩 윈도우 (값, 인덱스)
        swp = deque()
        for fv in range(k, m+1, c):
            # target이 미래 목적지 일 때, 탐색 범위 검사
            while swp and swp[0][1]<fv-2*d:swp.popleft()

            # 구간 최대값
            val = dp[i-1][fv]
            while swp and swp[-1][0]<=val:swp.pop()
            swp.append([val, fv])

            # 최적의 스콘 타이밍
            target = fv-d
            if target>0:dp[i][target] = swp[0][0]+taste(i, target)
        
        # 슬라이딩 윈도우에 들지 못한 나머지 구간
        etc = fv+c-d
        for fv in range(etc, m+1, c):
            while swp and swp[0][1]<fv-d:swp.popleft()
            if swp:dp[i][fv] = swp[0][0]+taste(i, fv)

for u in dp:print(u)
print(max(dp[-1]))