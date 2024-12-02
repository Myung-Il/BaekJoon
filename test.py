import sys
input = sys.stdin.readline

def updatefen(i):
  while i<=M:
    fen[i] += 1
    i += i&-i

def sumfen(i):
  SUM = 0
  while i:
    SUM += fen[i]
    i -= i&-i
  return SUM

for _ in range(int(input())):
    N = int(input()); M = 1<<17
    
    xlist = []; ylist = []  # x, y 에 대한 리스트
    for i in range(N):
        x,y = map(int,input().split())
        xlist.append([-x,0]); ylist.append((y,-x,i))
        # x 역방향, 0 // y x idx
    
    print(xlist, ylist)
    ylist.sort()    # y 정렬
    print(xlist, ylist)
    for i in range(N): # y의 idx값과 x의 idx값 맞추기
        xlist[ylist[i][2]][1] = i+1 # y좌표 압축
    print(xlist, ylist)
    xlist.sort() # x 정렬
    print(xlist, ylist)
    
    fen = [0]*(M+1); result = 0 # tree와 결과 저장할 변수 지정
    for x,i in xlist:
        result += sumfen(i)
        updatefen(i)
    
    print(result)