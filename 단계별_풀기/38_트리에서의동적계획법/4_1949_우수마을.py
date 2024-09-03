from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def solve(chile, parents):
    for elm in tree[chile]:
        if elm==parents:continue
        solve(elm, chile)
        dp[chile][0] += max(dp[elm][0], dp[elm][1]) # 우수마을이 아니라면 다음이 꼭 우수마을일 필요가 없다
        dp[chile][1] += dp[elm][0]                  # 우수마을이라면 다음은 무조건 그냥 마을이어야한다
                                                    # 단, 마을이 하나 이상 연결되어 있어야한다고 했는데
                                                    # 최대값을 구하고 있기 때문에 무조건 하나씩은 연결되어 있다
n = int(input())
num = list(map(int,input().split()))
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0], *([0, num[i]]for i in range(n))]
solve(1, 1)

print(max(dp[1]))