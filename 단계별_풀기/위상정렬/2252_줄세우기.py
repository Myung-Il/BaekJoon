from collections import deque
from sys import stdin
input=lambda:stdin.readline().rstrip()


n, m = map(int,input().split())
l = {elm:[] for elm in range(1, n+1)} # 무엇과 연결되어 있는지 기록
v = [0 for _ in range(n+1)]           # 몇개 연결되어 있는지 기록

for _ in range(m):
    a, b = map(int,input().split())
    l[a].append(b)
    v[b] += 1

q = deque([elm for elm in range(1, n+1)if not v[elm]])
# 딱히 순서 상관 없는 애들은 미리 출력할 예정

result = []
while q:
    x = q.popleft()  # 저장된 순서대로 가져옴
    result.append(x) # 순서대로 정렬되어 있기에 바로 저장

    for elm in l[x]: # 다음 연결된 요소 불러옴
        v[elm] -= 1  # 앞서 연결된 요소는 꺼냈으니 연결을 하나씩 줄여준다
        if not v[elm]:q.append(elm) # 연결된게 없다면 ~뒤에 있는게 아니니 이제 앞으로 꺼내준다

print(*result)