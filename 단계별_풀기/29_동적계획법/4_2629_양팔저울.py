from sys import stdin
input = lambda:stdin.readline().rstrip()

w = int(input())
weights = list(map(int,input().split()))
n = int(input())
beads = list(map(int,input().split()))


s = sum(weights)+1                # 한쪽 저울이 가질 수 있는 최대 무게
l = [[0]*(w+1) for _ in range(s)] # 1부터 최대 무게까지 무게추를 얼마나 맞출 수 있는지 확인하는 리스트

for xi in range(1, w+1):
    for yi in range(1, s):
        elm = l[yi-weights[xi-1]if yi>=weights[xi-1]else 0][xi-1]+weights[xi-1]
        # 현재 무게가 기록하려는 무게보다 무겁다면 지금이 더 무겁다는 소리니 0 값을 준다

        l[yi][xi] = max(l[yi-1][xi], l[yi][xi-1], 0 if elm>yi else elm)
        # 각 무게에 가장 근접한 값을 설정해준다


for elm in beads:
    flag = "N"     # 기준
    if elm>=s:pass # 만들 수 있는 최대 무게보다 크다면 차례를 넘김
    elif elm==l[elm][w]:flag = "Y" # 구슬과 같은 무게의 추가 있다면 Y로 바꾸고 넘김
    else:
        for yi in range(elm, s): # 무게추와 구슬의 조합으로 만들 수 있는 경우가 있는지 확인
            if l[yi][w]==elm+l[yi-elm][w]:flag = "Y";break # 있다면 Y로 바꾸고 넘김
    print(flag, end=' ')