from sys import stdin
input = lambda:stdin.readline().rstrip()

for _ in range(int(int(input()))):
    n = int(input())
    l = list(map(int,input().split()))
    k = list([0]*n for _ in range(n))

    for idx in range(1, n):                  # 본인은 더하지 않으니 1번째부터 대각선으로 이동
        k[idx-1][idx] = l[idx-1]+l[idx]      # 매칭되는 두 수를 합침
        for x in range(idx+1, n):            # l의 요소를 순회
            k[idx-1][x] = k[idx-1][x-1]+l[x] # 요소를 더해줌으로 파일 크기합을 만들어줌

    for x in range(2, n):    # 1번째는 이미 구했기 때문에 2부터 함
        for y in range(n-x): # 빈칸과 이미 구한 것은 제외하고 구해야 하기 때문에 구한 것들은 제외함
            k[y][x+y] += min([k[y][idx]+k[idx+1][x+y] for idx in range(y, x+y)])
        # 저장할 위치 += 최소값( 가로[idx를 기준으로 앞 값]+세로[뒷 값] idx를 1차원 위의 포인터)

    print(k[0][-1])