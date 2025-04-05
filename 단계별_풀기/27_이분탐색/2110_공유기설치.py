from sys import stdin
input = lambda:stdin.readline().rstrip()

n, c = map(int,input().split())
l = sorted([int(input())for _ in range(n)])

start = 1        # 비교하려는 시작 점
end = l[-1]-l[0] # 비교하려는 마지막 점

while start<=end:        # 만약 start가 end보다 더 크면 교차되는 순간이기에 멈춤
    mid = (start+end)//2 # 설치되는 간격

    cur, cnt = l[0], 1        # 현재값과 공유기 설치 횟수(처음에는 무조건 설치하니 1로 시작)
    for idx in range(1, n):   # 0번째는 무조건 설치하고 다음을 비교해야 됨
        if l[idx] >= cur+mid: # 다음 위치가 설치 간격보다 멀리 있다면
            cur = l[idx]      # 설치위치로 이동
            cnt += 1          # 설치함

    if cnt >= c:      # 만약 설치한 것이 더 많다면
        start = mid+1 # 시작 위치를 밀어서 좁은 범위에서 넓은 범위로 늘림
        result = mid  # 간격을 지정
    else:end = mid-1  # 반대로 마지막 위치를 당겨서 넓은 범위에서 좁은 범위로 줄임
print(result)         # 간격 출력