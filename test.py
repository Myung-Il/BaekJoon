import sys
input = sys.stdin.readline

A,B = "-"+input().rstrip(),"-"+input().rstrip()
dp = [[0]*(len(A)) for _ in range(len(B))]

for i in range(1,len(B)):
    for j in range(1,len(A)):
        if A[j] == B[i]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(dp[-1][-1])

i,j = len(B)-1,len(A)-1
ans = ""
while i>0 and j>0:
    if   dp[i][j] == dp[i][j-1]: j-=1
    elif dp[i][j] == dp[i-1][j]: i-=1
    else:
        ans = A[j] + ans
        i-=1; j-=1
if ans:
    print(ans)