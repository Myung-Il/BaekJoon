from sys import stdin, setrecursionlimit
from collections import deque
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def dfs(x, y): # 지금부터 섬을 찾을 거다
    if 0>x or x>=m or 0>y or y>=n: return False # 지도의 표기 범위를 넘어가면 아웃
    if land[y][x]:             # 섬이 있다면
        land[y][x] = 0         # 지도에서 섬이 있었다는 표시를 지우고
        make[y][x] = land_num  # 넘버링으로 바꿔준다
        island[land_num].append([x, y]) # 해당 섬의 좌표를 기록해준다
        for i in range(4): # 4방향 탐색
            xi = x+xl[i]
            yi = y+yl[i]
            dfs(xi, yi)    # 탐사를 보냄
        return True # 별 문제 없이 섬을 다 찾았다면 True
    return False    # 섬이 없다면 False

def bfs(il):                # 지금부터 다리의 길이와 어느 섬끼리의 다리인지도 구해야 한다
    for x, y in island[il]: # 우리가 탐색을 시작한 섬의 좌표를 꺼내온다
        for i in range(4):  # 4방향 탐색
            xi = x+xl[i]
            yi = y+yl[i]
            distance = 0    # 아직 거리는 0이다, 이후에 섬을 찾아서 다리를 놓으면 늘어난다
            while True:     # 다음 섬을 찾으러 간다
                if 0>xi or xi>=m or 0>yi or yi>=n: break # 범위를 벗어나면 아웃
                now = make[yi][xi] # 확인하려는 다음 좌표(이동경로)

                if now==il:break # 다음 위치가 같은 섬이면 넘어간다
                if now==0:       # 바다면
                    xi+=xl[i]    # 다리를 일단 놓는다
                    yi+=yl[i]    # 그 건너에 섬이 있을지도 모르니까 일단
                    distance+=1  # 다리를 놓아본다
                elif distance<2:break # 다리를 놨는데 1밖에 안되거나 놓을수가 없다? 아웃
                else:            # 다리의 길이가 1를 넘어가고 섬에 닿았다?
                    bridge.append([il, now, distance]) # 시작섬, 도착섬, 다리의 길이를 기록
                    break        # 섬 찾았으니까, 탈출

def find(e):
    if e!=parents[e]:
        parents[e] = find(parents[e])
    return parents[e]

def union(x, y, w):
    x = find(x) # 어느 섬을 거쳤는지 확인
    y = find(y) # 어느 섬을 거쳤는지 확인
    if x==y:return # 같은 섬을 거친적이 있다면 굳이 x와 y를 이을 필요가 없다 이미 이어져 있기 때문이다
    
    if x<y:parents[y] = x # 이어져 있지 않다면 이어준다
    else:  parents[x] = y # 숫자가 작은 섬을 기준으로 잡았다
    global s
    s+=w                  # 이어줬으니 길이를 추가한다


xl = [ 1,-1, 0, 0]
yl = [ 0, 0,-1, 1]

n, m = map(int,input().split())   # 지도의 세로 가로 입력
land = []                         # 지도
make  = [[0]*m for _ in range(n)] # 지도의 섬 번호를 표기할 것
visit = [[0]*m for _ in range(n)] # 지도의 바다를 포함한 모든 지점을 확인 했는지
for _ in range(n):                # 지도 입력
    land.append(list(map(int,input().split())))

island = [[]for _ in range(51)] # 섬이 얼마나 있을지 모르니 최대 갯수로 지정
land_num = 1                    # 섬을 1번부터 만들거
for yi in range(n):             # y의 좌표
    for xi in range(m):         # x의 좌표
        if dfs(xi, yi):         # 해당 좌표에 섬이 있는가 확인
            land_num+=1         # 있었다면 다음섬을 찾기위해서 섬 넘버링을 하나 올려줌

bridge = []                     # 섬끼리 다리를 놔줘야 됨
for il in range(1, land_num-1): # 모든 섬을 탐색해본다
    bfs(il)                     # 연결
bridge.sort(key=lambda x:x[2])  # 최소 총 다리 길이를 구해야하니 짧은 순으로 정렬한다

parents = [idx for idx in range(land_num)] # 이제 최소로 섬을 이을거다
s = 0                                      # 거리의 합을 기록할 변수
for a, b, w in bridge: # 출발, 도착, 거리
    union(a, b, w)     # 탐색

for elm in range(1, land_num):find(elm) # 탐색이 다 끝났는데 마지막에서야 두 섬을 이을 수 도 있다, 정리한다
print(s if s and len(set(parents))==2 else -1)