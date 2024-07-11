# n, m = map(int, input().split())
# memory = [0] + list(map(int, input().split()))
# cost = [0] + list(map(int, input().split()))
n, m = 5, 60
memory = [0, 30, 10, 20, 35, 40]
cost = [0, 3, 0, 3, 5, 4]
length = sum(cost)+1
dp = [[0 for _ in range(length)] for _ in range(n+1)]
ans = 10001

for i in range(1, n+1):
    ci, mi = cost[i], memory[i]
    for j in range(length):
        dp[i][j] = dp[i-1][j]
    for p in dp:print(p)
    for j in range(ci, length):
        dp[i][j] = max(dp[i-1][j-ci] + mi, dp[i][j])
        if dp[i][j] >= m:
            ans = min(ans, j)

for _ in dp:print(_)