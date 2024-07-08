import sys
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*(N) for _ in range(N)]

for term in range(1, N):
    for start in range(N):  # 첫행렬 : i, 끝행렬: i+term
        if start + term == N:  # 범위를 벗어나면 무시
            break

        dp[start][start+term] = int(1e9)  # 지금 계산할 첫행렬과 끝행렬
        
        for t in range(start, start+term):
            dp[start][start+term] = min(dp[start][start+term],
            							# 👇 1 + 2 + 3
                                        dp[start][t]+dp[t+1][start+term] + arr[start][0] * arr[t][1] * arr[start+term][1])

for d in dp : print(d)

'''

7
9 3
3 7
7 8
8 2
2 4
4 6
6 7

[0, 189, 384, 208, 280, 364, 466]
[0,   0, 168, 154, 178, 238, 328]
[0,   0,   0, 112, 168, 244, 342]
[0,   0,   0,   0,  64, 144, 244]
[0,   0,   0,   0,   0,  48, 132]
[0,   0,   0,   0,   0,   0, 168]
[0,   0,   0,   0,   0,   0,   0]


'''