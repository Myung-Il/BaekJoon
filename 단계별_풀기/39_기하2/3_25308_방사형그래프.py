from sys import stdin
input=lambda:stdin.readline().rstrip()

def solve():
    for i in range(8):                                   # 각각 볼록인지 확인 할거다
        a, b, c = i, (i+1)%8, (i+2)%8                    # 앞뒤로 있는 능력치 확인
        if g[a]*g[c]*2**0.5 >= g[b]*(g[a]+g[c]):return 0 # 넓이 ac/2 삼각형 = ak/2 + ck/2 = (a+c)k/2, k = ac/(a+c)
    return 1                                             # √2k(해당 거리까지는 180°를 만든다) < b(더 커야 180°보다 작아진다)
                                                         # ac√2/(a+c) < b, ac√2 < b(a+c)(볼록을 찾는 조건), ac√2 >= b(a+c)(볼록이 아닌 것을 찾는 조건)
def combination(e):
    if e==8:              # 8개의 능력치 전부 배치가 끝났다면
        global result
        result += solve() # 볼록 다각형인지 검사한다
        return

    for idx in range(8):       # 능력치 하나하나 돌려본다
        if visit[idx]:continue # 이미 본 능력치면 지나간다
        visit[idx] = 1         # 안 본거면 곧 볼 것이니 체크해준다
        g[e] = num[idx]        # 능력치 기록
        combination(e+1)       # 다음 능력치 보러 넘어간다
        visit[idx] = 0         # 봤으면 다시 꺼내준다


num = list(map(int,input().split())) # 방사형의 능력치
visit = [0]*8                        # 방문 처리
g = [0]*8                            # 방사형 그래프

result = 0     # 결과 값
combination(0) # 만들 수 있는 모든 방사형 그래프 구하는 함수
print(result)  # 결과에 대해서 출력