from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def solve(child, parents):
    for elm in tree[child]:
        if elm==parents:continue
        solve(elm, child)
        dp[child][0] += dp[elm][1]                  # 내가 아답터가 아니면 다음에는 아답터가 와야한다
        dp[child][1] += min(dp[elm][0], dp[elm][1]) # 내가 아답터라면 아답터가 오든 오지 않든 상관없다


n = int(input())
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 1]for _ in range(n+1)]
solve(1, 1)

print(min(dp[1]))