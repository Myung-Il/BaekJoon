import sys
from collections import deque
input = sys.stdin.readline

line1 = input().split()
N, M, C, D = map(int, line1)

line2 = input().split()
b = list(map(int, line2))

dp = [[0] * (M + 1) for _ in range(N)]
for k in range(M + 1):dp[0][k] = M - abs(b[0] - k)

for i in range(1, N):
    for j in range(C):

        dq = deque() 
        for k in range(j, M + 1, C):
            while dq and dq[0][1] < k - 2 * D:dq.popleft()

            val = dp[i-1][k]
            while dq and dq[-1][0] <= val: dq.pop()
            dq.append((val, k))


            target = k - D
            if target > 0:dp[i][target] = dq[0][0] + M - abs(b[i] - target)


        start_t = (k + C) - D
        for t in range(start_t, M + 1, C):
            limit_idx = t - D
            while dq and dq[0][1] < limit_idx:dq.popleft()
            if dq:dp[i][t] = dq[0][0] + M - abs(b[i] - t)

ans = 0
for k in range(M+1):
    if dp[N - 1][k] > ans:
        ans = dp[N - 1][k]

for o in dp:print(o)
print(ans)