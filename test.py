from sys import stdin
input = lambda:stdin.readline().rstrip()

def bt(e, dp):
    left, right = 0, len(dp)
    while left<right:
        mid = (left+right)//2
        if dp[0]>0 and dp[mid]>e:left=mid+1
        elif dp[0]<0 and dp[mid]<e:left=mid+1
        else:right=mid
    return right

def solve(dp, num, A, B, C):
    for idx in range(A, B, C):
        if dp[-1]>a[idx]:
            dp.append(a[idx])
            num.append(idx)
        else:
            point = bt(a[idx], dp)
            dp[point], num[point] = a[idx], idx
    return dp, num


n = int(input())
a = list(map(int,input().split()))

dp_f, f = solve([float("inf")], [0], n-1, -1, -1)
dp_b, b = solve([-float("inf")], [0], 0, n, 1)

print(dp_f[:0:-1], f[:0:-1])
print(dp_b[1:], b[1:])