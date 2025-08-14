from sys import stdin
input = lambda:stdin.readline().strip()

for _ in range(int(input())):
    n = int(input())
    game = list(map(int, input().split()))

    result = 0

    left, right = 0, n-1
    while left<right:
        remain = right-left
        if remain<4:
            if game[left] < game[right]:
                result += game[right]
                right -= 1
            else:
                result += game[left]
                left -= 1
        else:
            if game[left] < game[right] and :
                result += game[right]
                right -= 1
            else:
                result += game[left]
                left -= 1

'''
3 1 4 5
# 8

10 12 1 1 
# 13

끝 4개만 보면 될까?
1, 4번자리가 가장 클 경우, 그냥 더 큰거 가져가면 됨
문제는 2, 3번자리가 가장 클 경우임

50 100 ... 1 1 1
 2 100 ... 1 1 1

50을 먹어야 할지 아니면 그냥 계속 1을 먹어야할지 컴퓨터 입장에서는 알 수가 없음


10 12 100 50 13 1 1


'''