from sys import stdin
input = lambda:stdin.readline().rstrip()

while 1:
    n, *l = map(int,input().split())
    if n==0:break

    s, ans = [], 0                     # 스택과 결과값 선언
    for idx in range(n):               # 히스토그램 순회
        while s and l[s[-1]]>l[idx]:   # 스택이 비어 있고 기록되어 있는 값보다 작으면 실행
            x = s.pop()                # 이전에 저장된 위치 불러오기
            width = idx-s[-1]-1 if s else idx
                                       # 스택이 비어 있다면 [ 거리 0 부터 현재 위치까지 ]
                                       # 그렇지 않다면      [ 기록되어 있는 마지막 위치부터 현재위치까지
                                       #                     거리 차가 1 더 많기 때문에 -1까지 해준다   ]

            ans = max(ans, l[x]*width) # 최대 너비 결과 지정
        s.append(idx)                  # 현재 위치를 저장

    while s:
        x = s.pop()
        width = n-s[-1]-1 if s else n # [ 전체에서 현재 너비를 구하기 위해서
                                      #   1이 더 많기 때문에 -1 해준다       ]
        ans = max(ans, l[x]*width)
    
    print(ans)