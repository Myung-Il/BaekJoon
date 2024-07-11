# n,m = map(int,input().split())
# memory = list(map(int,input().split()))
# cost = list(map(int,input().split()))

n, m = 5, 60
memory = [30, 10, 20, 35, 40]
cost = [3, 0, 3, 5, 4]
dp = [[0 for i in range(n+1)]]
curCost = -1

while(max(dp[curCost]) < m):
    # 배열이 얼마나 길어질 지 모르므로 계산때마다 추가해준다.
    dp.append([0 for i in range(n+1)])
    curCost += 1
    
    for i in range(n):
        if cost[i] <= curCost:
            dp[curCost][i+1] = max(dp[curCost - cost[i]][i] + memory[i],dp[curCost][i])
        else:
            dp[curCost][i+1] = dp[curCost][i]

for _ in dp:print(_)