from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def dfs(e, m):
    left, right = 0, 0     # 트리를 왼쪽과 오른쪽으로만 구성하게 할 거임
    for elm, cost in l[e]: # 그러기 위해서는 가장큰 왼쪽과 오른쪽을 구분 해야 된다
        r = 0              # 트리 한쪽의 길이(왼쪽이나 오른쪽이 될 것)
        if not visit[elm]: # 방문된 적이 없다면
            visit[elm] = 1 # 방문 처리
            r = dfs(elm, cost) # 한쪽의 길이를 내려갈 수 있을 만큼 내려감(말단 까지 감)
        if left <= right: left = max(left, r) # 왼쪽부터 트리를 채움
        else: right = max(right, r)           # 가장 긴건 왼쪽이거나 오른쪽, 왼쪽이 오른쪽보다는 더 클 수는 없음

    global mx
    mx = max(mx, left+right)    # 최대 값을 설정해야 되는데 말단에서 올라오면서 왼쪽과 오른쪽 트리의 길이 기존에 찾은 것보다
                                # 길지도 모르니 기존의 합에서 왼쪽과 오른쪽을 더한 값으로 변경해준다, 짧으면 그대로 두고
    return max(left+m, right+m) # 왼쪽이든 오른쪽이든 말단에 도착하면 이전 노드와 현재 노드까지의 거리를 반환해준다
                                # 말단 노드가 아니라면 이전 노드와 현재까지의 거리 + 앞으로 가게 될 가장긴 긴 길이를 반환한다

n = int(input())
l = [[]for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(n):
    a, *v = map(int,input().split())
    for idx in range(0, len(v)-1, 2):
        l[a].append([v[idx], v[idx+1]])

mx = 0       # 최대 길이
visit[1] = 1 # 방문 설정
dfs(1, 0)    # 맨 위에서부터 내려다 볼거임
print(mx)