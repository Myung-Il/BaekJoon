from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().strip()
setrecursionlimit(10**6)

n = int(input())
farm = [0] + [int(input())for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]

def rice(day, start, end):                         # 처음에는 Top-down으로 내려간다
    if start>end:return 0                          # 찾는 값이 아니면 0
    if dp[start][end]:return dp[start][end]        # 이미 찾은 값이면 반환

    dp[start][end] = max(                          # 최대 찾기
        day*farm[start]+rice(day+1, start+1, end), # 왼쪽부터 계산했을 때
        day*farm[ end ]+rice(day+1, start, end-1)  # 오른쪽부터 계산했을 때
        )
    
    return dp[start][end]

print(rice(1, 1, n))