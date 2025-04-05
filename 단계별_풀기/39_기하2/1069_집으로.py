from sys import stdin
input=lambda:stdin.readline().rstrip()

x, y, d, t = map(int,input().split())
p = (x**2+y**2)**0.5

if d<t:print(p)                           # 도약이 느릴 때
else:                                     # 도약이 빠를 때
    n = p//d                              # 도약 횟수
    if p>d:print(min(n*t+p-n*d, t*(n+1))) # 도약하기에 거리가 너무 멀 때
                                          # 1. 최대한 도약해서 가고 남은 거리를 걸어간다
                                          # 2. 최대한 도약하고 마지막에 꺽어서 도약한다
    else:  print(min(p, t*2, t+d-p)) # 한번의 도약이 더 빠르거나 같을 때
                                     # 1. 걸어간다
                                     # 2. 꺽어서 도약한다
                                     # 3. 한번 도약하고 남은 거리는 걸어간다