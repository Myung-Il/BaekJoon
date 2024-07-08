import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
d = [[0 for i in range(n)] for i in range(n)]

# 인접한 2개의 행렬은 미리 곱하여 배열에 넣는다.
for i in range(n-1):
    d[i][i+1] = a[i][0]*a[i+1][0]*a[i+1][1]

def dp(start,end):
    if d[start][end] != 0:
        return d[start][end]
    if start == end:
        return 0
    
    r = float('inf')
    for i in range(start,end):
        temp = dp(start,i) + dp(i+1,end) + a[start][0]*a[i+1][0]*a[end][1]
        if r > temp:
            r = temp
    d[start][end] = r
    return r

print(dp(0,n-1))