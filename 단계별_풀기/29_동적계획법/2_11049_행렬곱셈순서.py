from sys import stdin
input = lambda:stdin.readline().rstrip()

n = int(input())
l = [list(map(int,input().split()))for _ in range(n)]

k = [[0]*n for _ in range(n)]

for idx in range(n-1): # 본인의 곱은 하지 않기때문에 1번째부터 함
    k[idx][idx+1] = l[idx][0]*l[idx][1]*l[idx+1][1]
    # 행렬곱을 대각선에 구한 후 저장

for x in range(2, n):    # 1번째는 이미 했기에 2번째부터 함
    for y in range(n-x): # 안 구한 자리를 찾아야 하기 때문에 이미 구한 만큼을 빼줌
        k[y][x+y] = min([k[y][idx]+k[idx+1][x+y] + l[y][0]*l[idx][1]*l[x+y][1] for idx in range(y, x+y)])
        # 저장할 위치 = 최소값( 가로[idx를 기준으로 왼쪽 계산이 끝난 값]+세로[오른쪽 계산이 끝난 값]
        #                      + 앞[현 위치 앞 수]*중앙[idx를 기준으로 곱 순서 바뀜]*뒤[현 위치의 뒷 수]
        #                      idx는 1차원 위 )
        #                      어차피 값은 곱하는 순서 때문에 가운데만 바뀜

for i in k:print(i)

'''
7
9 3
3 7
7 8
8 2
2 4
4 6
6 7
'''