from sys import stdin
input = lambda:stdin.readline().strip()


def pt(g):
    for i in dp:print(i)

n, m, c, d = map(int, input().split())
hit = list(map(int, input().split()))

dp = [[0]*n for _ in range(m+1)]
for i in range(m+1): dp[i][0] = i

res = 0
for k in range(m+1):
    s = m-abs(hit[0]-k)
    for i in range(1, n):
        scon, idx = 0, dp[k][i-1]
        for j in range(idx-d, idx+d+1, c):
            new = m-abs(hit[i]-j)
            if scon<=new: scon, idx = new, j

        dp[k][i] = idx
        s += scon
    res = max(res, s)
print(res)