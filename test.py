import sys; input = sys.stdin.readline

def ccw(a, b, c): # a-b-c가 반시계 방향인지 검사
    if (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0]) > 0:
        return True
    return False

def dist(a, b): # a-b 거리 계산 (제곱 형태로 반환)
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def solve():
    C = int(input())
    if C == 2: # 화살이 2개면 거리 계산하여 출력 후 프로그램 종료
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(dist(a, b) ** 0.5)
        return
    
    # 화살이 3개 이상이면 먼저 볼록 껍질을 구해야 한다.
    # monotone chain 알고리즘을 사용해서 구할 것이므로
    # 먼저 화살들이 x, y가 오름차순이 되게 정렬하자.
    arrows = sorted(list(map(int, input().split())) for _ in range(C))
    # 볼록 껍질의 아래
    convex_hull_down = []
    for i in range(C):
        while len(convex_hull_down) > 1:
            if ccw(convex_hull_down[-2], convex_hull_down[-1], arrows[i]):
                break
            convex_hull_down.pop()
        convex_hull_down.append(arrows[i])
    # 정렬된 반대로 탐색하여 볼록 껍질의 위를 구한다.
    convex_hull_up = []
    for i in range(C - 1, -1, -1):
        while len(convex_hull_up) > 1:
            if ccw(convex_hull_up[-2], convex_hull_up[-1], arrows[i]):
                break
            convex_hull_up.pop()
        convex_hull_up.append(arrows[i])
    # 두 볼록 껍질의 양 끝은 겹치기 때문에 겹치는 부분은 제외해서 합치자.
    # 겹치는 부분은 양 끝점이므로 회전하는 캘리퍼스의 시작점이 된다.
    lp, rp = 0, len(convex_hull_down) - 1
    convex_hull = convex_hull_down[:-1] + convex_hull_up[:-1] # 반시계 방향이 되게끔

    # 회전하는 캘리퍼스
    # 초기 답은 lp와 rp의 거리로 저장해두고 시작
    answer = dist(convex_hull[lp], convex_hull[rp])
    size = len(convex_hull) # 볼록 껍질의 크기
    for _ in range(size):
        lx, ly = convex_hull[lp]
        llx, lly = convex_hull[(lp + 1) % size]
        rx, ry = convex_hull[rp]
        rrx, rry = convex_hull[(rp + 1) % size]
        # 양 끝점과 그 점들의 반시계 방향의 다음 점과 벡터를 잡고
        # 두 벡터가 CCW이면 lp를 반시계 방향으로 한칸 이동
        # CW이면 rp를 반시계 방향으로 한칸 이동
        # 이를 볼록 껍질의 개수만큼 반복하면 된다.
        print(ccw([llx - lx, lly - ly], [0, 0], [rrx - rx, rry - ry]))
        if ccw([llx - lx, lly - ly], [0, 0], [rrx - rx, rry - ry]):
            lp = (lp + 1) % size
        else:
            rp = (rp + 1) % size
        answer = max(answer, dist(convex_hull[lp], convex_hull[rp])) # 돌릴 때마다 거리 갱신
    print(answer ** 0.5) # 답 출력

solve()