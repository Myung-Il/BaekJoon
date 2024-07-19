from sys import stdin
input = lambda:stdin.readline().rstrip()

def bellman_ford():
    distance[1] = 0          # 시작 0
    for circuit in range(n): # 마지막에 무한히 작아지는 확인 하기 위함
        for start, end, pay in graph:
            cost = pay+distance[start] # 지금까지 거리비용 + 다음까지의 비용
            if cost<distance[end]:     # 비용 비교
                distance[end] = cost   # 갱신
                if circuit==n-1:return True # 만약 마지막 음수 순환 때문에 더 작아진다면
    return False                            # 예외처리 해준다


n, m = map(int,input().split())
graph = [list(map(int,input().split()))for _ in range(m)] # 딕셔너리로 했다가 이렇게 바꿈
distance = [float("inf")for _ in range(n+1)] # bellman_ford의 반환 값을 참거짓으로 해놔서 꺼내 놔야 함

path = bellman_ford()
if path:print(-1)
else:
    for elm in range(2, n+1): # 분명 N번 도시로 가는 가장 빠른 시간을 순서대로 출력이라고 했는데
        print(-1 if distance[elm]==float("inf")else distance[elm]) # 정렬 그딴거 없이 되서 놀란 코드