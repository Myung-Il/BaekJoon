from sys import stdin
input=lambda:stdin.readline().rstrip()


n = int(input())
k = int(input())
dp = [[0]*(k+1) for _ in range(n+1)]

for ni in range(n+1):
    for ki in range(k+1):
        if not ki:  dp[ni][ki] = 1
        elif ki==1: dp[ni][ki] = ni
        else:
            dp[ni][ki] += dp[ni-1][ki]
            dp[ni][ki] += dp[ni-2][ki-1] if ni!=n else dp[ni-3][ki-1]
            dp[ni][ki] %= 1_000_000_003

print(dp)
print(dp[n][k])