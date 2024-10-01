from sys import stdin
input=lambda:stdin.readline().rstrip()


n = int(input())
k = int(input())
dp = [[0]*k for _ in range(n)]

for ni in range(n):
    dp[ni][0] = ni+1 # 색을 1개만 선택할 때는 색의 갯수만큼 선택 할 수 있다
    if ni<3:continue # 3개 이상부터 2개이상으로 씩 선택할 수 있다
    for ki in range(1, k):
        dp[ni][ki] = dp[ni-1][ki]+dp[ni-2][ki-1] # 점화식
        dp[ni][ki] %= 1_000_000_003

print(dp[-1][-1])