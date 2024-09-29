from sys import stdin
input = lambda:stdin.readline().rstrip()
INF = float("inf")


def bit(cnt, x, visit):
    if cnt==n-1:       return l[x][0]if l[x][0]else INF # 순환이 된다면 저장하는데 안된다면 버린다
    if dp[x][visit]!=0:return dp[x][visit]              # 이미 방문했다면 방문했던 값을 반환

    mn = INF                # 아주 큰 무언가
    for idx in range(1, n): # 하나씩 비교
        if visit&1<<idx or l[x][idx]==0:continue                # 이미 방문했거나 갈 수 없다면 넘긴다
        mn = min(mn, bit(cnt+1, idx, visit|1<<idx) + l[x][idx]) # 최소값 기록( 기존, 다음 장소 + 현재 장소 )
    dp[x][visit] = mn   # 최소값 갱신
    return dp[x][visit] # 결과 반환


n = int(input())
l = [list(map(int,input().split()))for _ in range(n)]
dp = [[0]*(1<<n)for _ in range(n)]

print(bit(0, 0, 1))