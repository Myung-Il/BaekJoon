from sys import stdin
input = lambda:stdin.readline().rstrip()

n, B = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]

def dac(s,b):
    if b == 1: return s
    a = dac(s,b//2)
    
    cal = [[0]*n for _ in range(n)]
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                cal[i][j] += (a[i][k]*a[k][j])%1000
    if b % 2:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += (cal[i][k]*A[k][j])%1000
    else:return cal
    return result

for i in dac(A,B):
    for j in i:
        print(j%1000, end =" ")
    print()

'''
2 7
1 1
1 1

2 5
1 1
1 1

2 4
1 1
1 1

2 3
1 1
1 1

2 2
1 1
1 1

2 1
1 1
1 1
'''