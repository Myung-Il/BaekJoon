from sys import stdin                    # sys 모듈 불러옴
input = lambda:stdin.readline().rstrip() # input을 변형

n, k = map(int,input().split()) # 입력 저장
p = 1000000007                  # 나눌 수

def factorial(num):             # 팩토리얼 함수
    result = 1                  # 초기값
    for i in range(2, num+1):   # 현재 n값 도출
        result = result * i % p # 계산
    return result               # 결과 반환

# a == k!(n-k)!
# a**(p-1) = 1 mod p
# a**(p-2) = a**-1 mod p
def power(num, P):              # a와 p를 받음
    if P == 1:return num % p    # a**1를 반환
    
    # 제곱 분활 과정 : 3**13 -> 3(3**12) -> 3(3**6)**2
    #                 3**6  -> (3**3)**2
    #                 3**3  -> 3(3**2)
    #                 3**2  -> (3**1)**2
    if P%2:return (power(num,P//2)**2 * num) % p # f가 홀수인 경우 : a * ( a**( ( p-1 )/2 ) )**2
    else:  return (power(num,P//2)**2)       % p # f가 짝수인 경우 :     ( a**( p/2 ) )**2

# n!*(k!(n-k)!)**(p-2)%p
print(factorial(n) * power((factorial(k) * factorial(n-k)), p-2) % p)