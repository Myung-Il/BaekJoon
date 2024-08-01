import sys
input=sys.stdin.readline

def Distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

N=int(input())
W=int(input())

a=[[0,0]]
b=[[N-1  ,N-1]]
for _ in range(W):
    i,j=map(int,input().split())
    a.append([i-1,j-1])
    b.append([i-1,j-1])
dp=[[float('inf') for _ in range(W+1)] for _ in range(W+1)]
dp_trace=[[0 for _ in range(W+1)] for _ in range(W+1)] #어디에서 왔니
#print(a)
dp[0][0]=0
ans=[]

#O(W^3)
for y in range(W+1):
    for x in range(W+1):
        if y==x: continue
        if y < x:
            if y and x-1==y:
                for k in range(x-1):
                    if dp[y][x]>dp[y][k]+Distance(b[x], b[k]):
                        dp[y][x]=dp[y][k]+Distance(b[x], b[k])
                        dp_trace[y][x]=k
            else:
                dp[y][x]=dp[y][x-1]+Distance(b[x], b[x-1])
                dp_trace[y][x]=x-1
        else:
            if x and y-1==x:
                for k in range(y-1):
                    if dp[y][x]>dp[k][x]+Distance(a[y], a[k]):
                        dp[y][x]=dp[k][x]+Distance(a[y], a[k])
                        dp_trace[y][x]=k
            else:
                dp[y][x]=dp[y-1][x]+Distance(a[y], a[y-1])
                dp_trace[y][x]=y-1

compare=float('inf')
I,J=0,0

for i in range(W):
    if dp[i][W]<compare: I,J = i,W; compare=dp[i][W]
    if dp[W][i]<compare: I,J = W,i; compare= dp[W][i]
    
print(*dp, sep='\n')
print(*dp_trace, sep='\n')
for i in range(W):
    if J>I:
        J=dp_trace[I][J]
        ans.append(2)
    else:
        I=dp_trace[I][J]
        ans.append(1)
for i in range(W-1,-1,-1):
    print(ans[i])