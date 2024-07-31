from sys import stdin
input = lambda:stdin.readline().rstrip()

s1 = list(input())
s2 = list(input())

a, b = len(s1)+1, len(s2)+1
dp = [[0]*a for _ in range(b)]
for yi in range(1, b):
    for xi in range(1, a):
        if s1[xi-1]==s2[yi-1]:dp[yi][xi] = dp[yi-1][xi-1]+1 # 접두사 같디면 이전의 결과 +1
        else:dp[yi][xi] = max(dp[yi-1][xi], dp[yi][xi-1])   # 다르다면 최대 값을 가져온다
print(dp[-1][-1])

x, y, ans = a-1, b-1, ""
while x>0 and y>0:
    if   dp[y][x] == dp[y][x-1]: x-=1 # 접두사가 다르니 같아질 때까지 이전 값으로 이동한다
    elif dp[y][x] == dp[y-1][x]: y-=1 # 접두사가 다르니 같아질 때까지 이전 값으로 이동한다
    else:                             # x는 이전 영단어를 찾고
        ans += s1[x-1]                # y는 LCS의 최소 시작 지점을 찾는다
        x-=1
        y-=1
        
if ans:print(ans[::-1])