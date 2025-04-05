from sys import stdin
input = lambda:stdin.readline().rstrip()

n = int(input())
l = list(map(int,input().split()))


def BT(elm):
    left, right = 0, len(LIS)    # 탐색 범위
    while left<right:            # 탐색 범위를 넘어가면 멈춤
        middle = (left+right)//2 # 중앙 위치
        if LIS[middle]<elm:left = middle+1
                            # 추가하려는 값이 탐색 값보다 크다면 왼쪽 포인터로 오른쪽으로 옮김
        else:right = middle # 추가하려는 값이 탐색 값보다 작다면 오른쪽 포인터로 왼쪽으로 옮김
                            # 만약 두 값이 같아진다면 elm가 들어갈 위치를 찾았다는 뜻이니 반복을 멈춘다
    return right            # (left==middle+1)와 (right==middle)가 값은 값을 가르킴

LIS = [0]
for elm in l: # 우리가 알고자 하는 증가 수열 요소를 하나씩 받음
    if LIS[-1]<elm:LIS.append(elm) # 마지막 요소보다 크면 추가
    else:LIS[BT(elm)] = elm        # 최소를 갱신해줌
print(len(LIS)-1)


f"""
5
5 1 4 2 3

6
10 20 10 30 20 50
"""