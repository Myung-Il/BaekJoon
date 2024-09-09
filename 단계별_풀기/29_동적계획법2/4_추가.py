from sys import stdin
input = stdin.readline

n, w = int(input()), list(map(int, input().split())) # 추의 갯수와 추의 무게 리스트
m, b = int(input()), list(map(int, input().split())) # 구슬의 갯수와 구슬의 무게 리스트


# 추의 최대 무게 500 추의 개수 n
dp = [[0 for _ in range((500 * j)+1)] for j in range(n+1)]
ans = []

def cal(num, weight): # 추로 판별할 수 있는 구슬의 무게를 나타내는 함수
    print(num, weight)
    if num > n:return # 구슬의 숫자가 주어진 구슬보다 크다면 return
    if dp[num][weight] == 1: # 이미 같은 추의 무게와 개수로 방문했다면 return
        return
    dp[num][weight] = 1

    cal(num+1, weight + w[num-1])      # [이전 추의 무게]와 [현재 추의 무게] 합 추가
    cal(num+1, weight)                 # 그 자리에 추 추가
    cal(num+1, abs(weight - w[num-1])) # [이전 추의 무게]와 [현재 추의 무게] 차 추가
                            # 0번째부터가 아닌 -1번째부터 하는 이유는 +1로 했을 경우
                            # dp의 마지막에 도착했을 때 indexError가 뜨기 때문이다

cal(0, 0)

for bead in b:
    if bead > 500 * n:
        ans.append('N')
    elif dp[n][bead] == 1:  
        ans.append('Y')
    else:
        ans.append('N')

print(*ans)