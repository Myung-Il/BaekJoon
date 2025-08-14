from sys import stdin
input = lambda:stdin.readline().strip()

T = int(input())

for t in range(T):
    N = int(input())                               # 카드의 갯수
    arr = list(map(int, input().split()))          # 카드들
    dp = [[0 for _ in range(N)] for _ in range(N)] # dp 리스트

    turn = True if N%2 else False
    # 카드의 갯수가 홀수라면 근우의 차례다

    for size in range(N):
        for i in range(N - size):
            if size == 0: dp[i][i+size] = arr[i] if turn else 0
            elif turn: dp[i][i+size] = max(dp[i+1][i+size] + arr[i], dp[i][i+size-1] + arr[i+size])
            else: dp[i][i+size] = min(dp[i+1][i+size], dp[i][i+size-1])
            
        turn = not turn #차례바꿈

    print(dp[0][N-1])