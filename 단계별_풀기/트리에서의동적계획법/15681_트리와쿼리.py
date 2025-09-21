from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def g(node, bf):
    dp[node][1] += num[node-1] # 0번은 독립이 아닐 때, 1번은 독립일 때, 뭐든 시작하면 독립이기 때문에 가중치를 더한다
    path[node][1].append(node) # 경로에 현재 노드를 기록한다

    for elm in tree[node]:    # 다음에 갈 수 있는 곳을 뽑는다
        if elm==bf:continue   # 부모 노드로는 못 간다
        result = g(elm, node) # 다음 경로를 가져온다
        dp[node][0] += max(dp[elm][0], dp[elm][1]) # 현재 독립아니면 다음으로는 "독립" 또는 "독립아님"이 올 수 있다
        dp[node][1] += dp[elm][0]                  # 현재 독립이면 다음으로는 "독립아님"만 올 수 있다

        path[node][1] += result[0]                          # 현재 독립이면 독립아님 경로밖에 못 받는다
        if dp[elm][0]>dp[elm][1]:path[node][0] += result[0] # 현재 독립이 아니라면 다음에 오는 경로가
        else:                    path[node][0] += result[1] # "독립"이거나 "독립아님" 둘 중에서 더 큰 것으로 받으면 된다
    return path[node] # 어디를 지나쳐왔는지 반환한다

#                   path             dp
# g( 5, 4) =      [], [5]           0,  20
# g( 4, 3) =     [5], [4]          20,  10
# g( 3, 2) =     [4], [3 5]        20,  60
# g( 2, 1) =   [3 5], [2 4]        60,  50
                  
# g( 7, 6) =      [], [7]           0,  70
# g( 6, 2) =     [7], [6]          70,  20
# g( 2, 1) = [3 5 7], [2 4 7]     130, 120
# g( 1, 1) = [2 4 7], [1 3 5 7]   130, 140



n = int(input())
num = list(map(int, input().split())) # 가중치
tree = [[]for _ in range(n+1)]        # 트리
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0]for _ in range(n+1)]                  # 이전 값이 독립일 때와 아닐 때 기록할 리스트
path = [[[]for _ in range(2)]for _ in range(n+1)] # 어떤게 독립이였는지 지록할 리스트
g(1, 1)

if dp[1][0]>dp[1][1]:
    print(dp[1][0])
    print(*sorted(path[1][0]))
else:
    print(dp[1][1])
    print(*sorted(path[1][1]))