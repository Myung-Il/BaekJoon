from sys import stdin
input=lambda:stdin.readline().rstrip()


def bit(x, visit):                    # 현재 몇번째 사람인가, 방문처리
    if x==n:         return 0         # 3명다 일하게 되었을때
    if dp[visit]!=-1:return dp[visit] # 이미 방문한 적이 있다면 패스

    mn = float("inf")            # 최소를 구하기 위한 그냥 아주 큰 무언가
    for idx in range(n):         # 비용을 하나씩 비교할 것이다
        if visit&1<<idx:continue # 물론 이미 하는 일이 있다면 넘긴다
        mn = min(mn, bit(x+1, visit|1<<idx)+l[x][idx]) # 이미 최소 비용으로 일하고 있을 수 있고
    dp[visit] = mn   # 최소값을 기록한다                # 아니라면 idx번 일을 선택하고 다음 사람에게 차례를 넘긴다
    return dp[visit] # 최소값을 반환한다


n = int(input())
l = [list(map(int,input().split()))for _ in range(n)]
dp = [-1]*(1<<n) # 전등 스위치는 꺼짐(0)과 켜짐(1) 두가지 경우를 가지고 있다
                 # 지금은 일을 받지 않았느냐(0), 받았느냐(1)이다
                 # 만약 그런 사람이 3명이면 000(0)에서 111(7)까지 경우의 수가 있다
print(bit(0, 0)) # 근데 아무도 일을 하지 않는 경우는 없으니 그곳에 최소값을 저장한다