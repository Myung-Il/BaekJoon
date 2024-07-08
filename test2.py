import sys
input = sys.stdin.readline

for i in range(1):
    n = 15
    f = list(map(int,"1 21 3 4 5 35 5 4 3 5 98 21 14 17 32".split()))
    d = list([0]*n for _ in range(n))
    
    for i in range(n-1):
        d[i][i+1] = f[i] + f[i+1]
        for j in range(i+2,n):
            d[i][j] = d[i][j-1] + f[j]

    for v in range(2,n):
        for i in range(n-v):
            j = i+v
            d[i][j] += min([d[i][k] + d[k+1][j] for k in range(i,j)])
    
    for i in d:print(*i)