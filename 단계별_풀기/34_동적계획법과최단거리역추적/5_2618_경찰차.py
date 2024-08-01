from sys import stdin
input = lambda:stdin.readline().rstrip()

def Distance(a, b): # a지점과 b지점의 거리 계산
    return abs(a[0]-b[0])+abs(a[1]-b[1])

n = int(input()) # 도로의 개수
w = int(input()) # 사건의 수( 지점 수 )

a = [[1, 1]] # 1번 경찰차
b = [[n, n]] # 2번 경찰차
for _ in range(w): # 각 경찰차가 갈 수 있는 지점
    x, y = list(map(int,input().split()))
    a.append([x, y])
    b.append([x, y])
dp = [[float("inf")]*(w+1) for _ in range(w+1)]
                # inf를 기준으로 (i, i)로 이루어진 가상의 대각선을 그어준다
                # 우삼각은 2번 경찰차의 지점간의 거리를 기록할 것이며
                # 좌삼각은 1번 경찰차의 지점간의 거리를 기록할 것이다

dp[0][0] = 0                          # 아직 이동을 하지 않았기에 0에서 시작한다
back = [[0]*(w+1)for _ in range(w+1)] # 몇번째 사건에서 왔는지 기록할 것이다
ans = []                              # 마지막에 기록한 사건을 역으로 추적하면서
                                      # 1번 경찰차인지 2번 경찰차인지 저장할 것이다

for y in range(w+1):
    for x in range(w+1):
        if x==y:continue     # (i, i)는 확인하지 않는다, 왜냐면 1번차인지 2번차인지 확인 할 수 없기때문이다
        if x>y:              # 2번차가 이동한다면
            if y and x-1==y: # 1번차가 이동한적 있다면     ex) 1번차는 2지점에 있다
                for k in range(x-1):                     # 다양한 방법으로 2지점으로 온 1번차의 각 거리를
                    path = dp[y][k]+Distance(b[x], b[k]) # 2번차의 2 -> 3 거리와 더한다
                    if dp[y][x]>path:                    # 더했는데 더 짧은 루트가 있다?
                        dp[y][x] = path                  # 거리 갱신
                        back[y][x] = k                   # 2번차가 어디서 왔는지 기록
                                                            # 1번차가 1지점을 경유했는지 알 수 없음
                                                            # case1 : 1번차(0~2) -> 2번차(2~3)
                                                            # case2 : 2번차(0~1) -> 1번차(1~2) -> 2번차(2~3)
                                                            # 각 case거리를 계산해서 짧은 것을 찾아야함
            else:
                dp[y][x] = dp[y][x-1]+Distance(b[x], b[x-1]) # 지금까지 온 거리 + 다음 지점까지의 거리
                back[y][x] = x-1                             # 2번차는 그냥 다음 지점으로 온 것이니 이전 지점이 온 곳이다
        else:
            if x and y-1==x: # 2번차가 이동한 적이 있다면, 위와 동일하게 
                for k in range(y-1):                     # 다양한 방법으로 이전 지점까지 온 각 거리를
                    path = dp[k][x]+Distance(a[y], a[k]) # 다음 지점까지의 거리와 더해준다
                    if dp[y][x]>path:                    # 짧은 것을 발견하면
                        dp[y][x] = path                  # 갱신
                        back[y][x] = k                   # 1번차의 이전 지점 기록
            else:
                dp[y][x] = dp[y-1][x]+Distance(a[y], a[y-1]) # 지금까지 온 거리 + 다음 지점까지의 거리
                back[y][x] = y-1                             # 1번차는 다음 지점으로 한번 이동했기 때문에 온 곳은 이전 지점이다

pin, x, y = float("inf"), 0, 0 # 최소 값을 찾기 위해서 기록할 변수와 그 값의 자리를 찾을 것이다
for i in range(w):             # 지점의 개수만큼만 이동했기 때문에 w만큼 확인을 한다
    if dp[i][w]<pin: pin, x, y = dp[i][w], w, i # 2번차를 마지막으로 이동했을 때, 최소가 있다면
    if dp[w][i]<pin: pin, x, y = dp[w][i], i, w # 1번차를 마지막으로 이동했을 때, 최고가 있다면

for _ in range(w):
    if x>y:            # (i, i)를 기준으로 마지막 이동을 1번차인지 2번차인지 구분
        x = back[y][x] # 2번차인 경우 어디서 왔는지 확인하고 역추적
        ans.append(2)  # 2번차 이동했으니 기록
    else:
        y = back[y][x] # 1번차가 어디서 왔는지 역추적
        ans.append(1)  # 1번차가 이동했으니 기록

print(pin)                  # 최소값 출력
print(*ans[::-1], sep='\n') # 역추적했느니 값이 뒤집어져 있음