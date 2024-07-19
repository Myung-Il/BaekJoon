import sys


input = lambda: sys.stdin.readline().rstrip()
MAX = 100000000
n, m = map(int, input().split())

dist = [MAX for _ in range(n + 1)]
edge = [tuple(map(int, input().split())) for _ in range(m)]


def bf():  # bellman-ford
    dist[1] = 0
    for i in range(n):  # n-1 번 돌고, 마지막 n번째에는 갱신되면 음의 싸이클 있는지 보는 것
        for e in edge:
            frm, to, cost = e
            if dist[frm] != MAX and dist[to] > dist[frm] + cost:
                dist[to] = dist[frm] + cost  # 값 갱신
                if i == n - 1:  # 만약 n번째 시도에도 값 갱신됐으면
                    print("===", i, n-1)
                    return 1  # 음의 싸이클 존재

    return 0  # 음의 싸이클 존재하지 않음


if bf():
    print(dist)
    print(-1)
else:
    print(dist)
    for i in range(2, n + 1):
        print(-1 if dist[i] == MAX else dist[i])