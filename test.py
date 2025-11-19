from sys import stdin
input = lambda:stdin.readline().strip()

n, m, c, d = map(int, input().split())
hit = list(map(int, input().split()))
dp = [[0]*(m+1)for _ in range(n)]

def taste(i, t):return m-abs(hit[i]-t)

for i in range(n):
    for t in range(m+1):
        for k in range(t-d, t+d+1, c):
            if k<0 or m<k:continue
            dp[i][t] = max(dp[i][t], taste(i, t)+dp[i-1][k])

print(max(dp[-1]))