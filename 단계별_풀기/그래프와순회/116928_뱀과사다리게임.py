from collections import deque
from sys import stdin
input = lambda:stdin.readline().rstrip()

n, m = map(int,input().split())
dc = {i:i for i in range(1, 101)}   # 각 번호 이동 대상
for _ in range(n+m):                # 1->1 or 1->99같은 것을 저장
    a, b = map(int,input().split()) # 위의 이동 대상을 설정
    dc[a] = b
visit = [False]*101 # 반문 확인
visit[1] = True     # 시작은 1부터

d = deque([[1,0]])  # 현재 위피, 이동 횟수
while d:
    now, length = d.popleft()
    if now==100:break
    
    for dice in range(1, 7): # 주사위는 1~6까지 눈을 가지고 있음
        dn = dice+now        # 다음 칸 번호
        if dn>100 or visit[dn]:continue # 판의 최대 크기를 벗어나거나 방문했다면 넘김
        visit[dn] = True                # 방문 확인
        d.append([dc[dn], length+1])    # 다음 칸 입력, 이동 횟수 추가

print(length) # 최종 이동 횟수 출력