from sys import stdin
input=lambda:stdin.readline().rstrip()


def factorial(x):
    if x==1:return 1
    return x*factorial(x-1)

def gcd(a, b):
    if a==0:return b
    return gcd(b%a, a)

def bit(lth, x, visit):    # 현재 순열의 길이, 나머지 상태, 방문 처리
    if visit == (1<<n)-1:  # 전부 방문 했을 때
        if not x: return 1 # 나머지가 없다면 정답을 맞출 수 있는 가능성 중 하나라는 말이다, 가능성 1 추가
        else:     return 0 # 나머지가 있다면 정답을 맞출 가능성이 없다는 말이다, 0 반환
    if dp[visit][x]!=-1:return dp[visit][x] # 이미 있다면 그대로 반환

    for idx in range(n):
        if visit&1<<idx:continue # 방문 했다면 넘어간다
        dp[visit][x] += bit(lth+length[idx], (x+cbi[idx][lth])%k, visit|1<<idx)
        # 가능성 기록 += bit( 현재 길이 증가, 나머지 갱신, 방문 설정 )
    dp[visit][x] += 1   # dp가 -1이기 때문에 +1을 해준다, 가능성이
    return dp[visit][x] # 있거나 1> 없거나 0 이어야하는데 -1은 아직 계산하지 않았음이니 초기화 해준다


n = int(input())                # 집합의 수
l = [input()for _ in range(n)]  # 자연수 집합
element= [int(elm)for elm in l] # 정수화 저장
length = [len(elm)for elm in l] # 자연수의 길이를 저장
k = int(input())                # 나누어 떨어지는 수

cbi = [[elm*10**num % k for num in range(sum(length))]for elm in element]
# 각 자연수의 순열의 위치를 사전에 만들어서 기록 : 각 자리수씩 확인, 정확히 얼마씩 차이나는지 모르기 때문
dp = [[-1]*k for _ in range(1<<n)] # 나머지에 따른 가능성 리스트

p = bit(0, 0, 0)  # 그렇게 얻어낸 모든 가능성
q = factorial(n)  # 집합의 모든 조합의 경우의 수
if p:             # 가능성이 있다면
    g = gcd(p, q) # 최대공배수를 구하여
    print(f"{p//g}/{q//g}") # 기약분수 형태로 나타낸다
else:print("0/1")           # 가능성이 없다면 0/1형태로 나타낸다