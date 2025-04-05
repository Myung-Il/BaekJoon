from sys import stdin
input = lambda:stdin.readline().rstrip()

# MITM : 완전탐색을 하기에는 무리가 있을 때 사용하며
#        연산을 줄이기위해서 절반으로 나눠서 계산하는 방식이다

n, c = map(int,input().split())
w = list(map(int,input().split()))
w1, w2 = w[:n//2], w[n//2:]
a, b = [], []

def bf(arr, seq, idx, sum): # 완전탐색
    if len(arr) == idx:     # arr에 있는 것만큼만 계산할 수 있기 때문에
                            # arr의 길이와 재귀횟수가 같다면
        seq.append(sum)     # 현재 합을 seq에 넣어준다
        return seq          # 그리고 반환해준다
    
                                      # 현재값과 이후의 값을 더할지 결정함
    bf(arr, seq, idx+1, sum)          # 더하지않고 넘감
    bf(arr, seq, idx+1, sum+arr[idx]) # 더하고 넘김
    return seq                        # 결과 반환

a = bf(w1, a, 0, 0)
b = sorted(bf(w2, b, 0, 0))
result = 0

for elm in a:
    if c < elm:continue

    left, right = 0, len(b)
    while left < right:
        middle = (left+right)//2
        if b[middle] <= c-elm: left = middle+1
        else: right = middle
    
    result += left
print(result)