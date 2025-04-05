from sys import stdin
input = lambda:stdin.readline().rstrip()


def sumRange(y):
    SUM = 0
    while y:
        SUM += fenwick[y] # 해당 섬이 포함된 모든 구간을 줄인다
        y -= y&-y         # y의 비트값에서 최하위에 있는 1이 나타내는 값
    return SUM            # 위의 값을 역순으로 돌아가며 줄여준다

def update(y):
    while y <= 2**17:   # 모든 구간을 갱신 해줄건데
        fenwick[y] += 1 # y의 비트값에서 최하위에 있는 1이 나타내는 값
        y += y&-y       # 위의 값을 구분 할 수 있는 곳만 갱신해준다


for _ in range(int(input())):
    n = int(input())
    xl, yl = [], []
    for idx in range(n):
        x, y = map(int,input().split())
        xl.append([-x, 1])      # 북서방향을 북동으로 바꿔서 계산하기 편하게 만든다
        yl.append([y, -x, idx]) # 정렬 순서 y, x이며 idx는 몇번째 섬인지를 알려준다 ==> y 압축
    yl.sort()                   # y 정렬

    for idx in range(n):         # y에 대한 정렬이 끝났으니 압축한 y값을
        xl[yl[idx][2]][1] += idx # x에 옮겨주는 작업을 해준다
    xl.sort()                    # x 정렬
    
    fenwick = [0]*2**18 # 펜윅 트리를 사용할 것이다, 기존의 세그먼트와는 다른게
    result = 0          # 단점이 많지만 누적합을 구하기 좋기 때문이다
    for _, y in xl:     # 참고로 첫번째 섬은 어차피 오는 섬이 없기 때문에 0이라서 더할게 없다
        result += sumRange(y)
        update(y)
    print(result)