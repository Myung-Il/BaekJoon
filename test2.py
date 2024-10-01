import sys
from math import gcd, factorial

n = int(sys.stdin.readline())                              # 몇개 입력
stack = []
for _ in range(n): stack.append(int(sys.stdin.readline())) # 숫자
long = []
for i in stack: long.append(len(str(i)))                   # 숫자의 길이
k = int(sys.stdin.readline())                              # 나머지
dp = [[-1] * k for _ in range(1 << n)]                     # 다이나믹 프로그래밍
rm = [[-1] * (sum(long)) for _ in range(n)]                # 조합들을 기록하는 리스트인 듯
for i in range(n):                                         # 입력한만큼
    for j in range(sum(long)):                             # 최대 길이만큼
        rm[i][j] = (stack[i] * 10**j) % k                  # 조합을 만듬
print(len(dp), len(dp[0]))
print(rm)


def dfs(L, visited, rest):      # 현재 길이, 방문, ?
    if visited == (1 << n) - 1: # 전부 탐색하면
        if rest == 0: return 1  # ?
        else:         return 0  # ?

    if dp[visited][rest] != -1:  # 방문 했다면
        return dp[visited][rest] # 기록값 주기
    
    for i in range(n):              # 하나씩 방문
        if visited & (1 << i) == 0: # 이미 방문 했던 거면 넘김
            dp[visited][rest] += dfs(L + long[i], visited | (1 << i), (rest + rm[i][L]) % k)
            # 데이터 누적  += dfs(길이증가, 방문처리, )
    dp[visited][rest] += 1
    return dp[visited][rest]


temp = dfs(0, 0, 0)
F = factorial(n)
print(dp, temp, F)
if temp == 0: print('0/1')
else:
    v = gcd(F, dp[0][0])
    print('{}/{}'.format(temp//v, F//v))