from sys import stdin
input=lambda:stdin.readline().rstrip()


log = 18                              # log2_500,000 < 262,144 == 2**18
m = int(input())                      # 함수에 들어갈 테스트케이스 갯수
dp = [[0]*(m+1)for _ in range(log+1)] # 다이나믹 프로그래밍


dp[0] = [0]+[*map(int,input().split())] # 테스트케이스 입력
for lvl in range(1, log+1):             # 2배수로 다음 요소를 찾을 거임
    for idx in range(1, m+1):           # 테스트케이스 인덱스 위치 찾기
        dp[lvl][idx] = dp[lvl-1][dp[lvl-1][idx]] # 찾은 요소 넣기

q = int(input())
for _ in range(q):
    n, x = map(int,input().split())
    for bit in range(log, -1, -1): # 100 000 000 000 000 000 (이진수)
        if n & (1 << bit):         # n을 단항 구조 트리라고 생각 할 때
            x = dp[bit][x]         # 최대한 많은 구간을 뛰어넘어서 찾아가면 됨
    print(x)