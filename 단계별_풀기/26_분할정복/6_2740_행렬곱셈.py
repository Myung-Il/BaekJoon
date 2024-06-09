from sys import stdin
input = lambda:stdin.readline().rstrip()

a1, b1 = map(int,input().split())
l1 = [list(map(int,input().split()))for _ in range(a1)]

a2, b2 = map(int,input().split())
l2 = [list(map(int,input().split()))for _ in range(a2)]

answer = [[0]*b2 for _ in range(a1)]
for i in range(a1): 
    for j in range(b2): 
        for k in range(b1): 
            answer[i][j] += l1[i][k] * l2[k][j]

for ans in answer:print(*ans)