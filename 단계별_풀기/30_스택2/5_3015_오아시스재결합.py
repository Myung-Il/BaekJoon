from sys import stdin
input = lambda:stdin.readline().rstrip()

n = int(input())
l = [int(input())for _ in range(n)]

cnt = 0
stk = [] # ( 현재값, 연속된 횟수 )
for elm in l:
    while stk and stk[-1][0]<elm: # 이전 값보다 크다면
        cnt += stk.pop()[1]       # 작은 애들은 전부 꺼내고 횟수만큼 더한다
        
    if stk and stk[-1][0]==elm:   # 만일 중복이라면
        size = stk.pop()[1]       # 꺼내고
        cnt += size               # 이전의 마주보는 경우를 더 해주고
        if stk:cnt+=1             # 현재값이 제일 크지 않다면 +1
        stk.append([elm, size+1]) # 연속된 횟수를 늘려줌
    else:                   # 중복이 아닐 경우
        if stk:cnt+=1       # n이 1일수도 있으니 if를 달아줌
        stk.append([elm,1]) # 이전 값보다 작아서 현재와 이전의 관계만 따질 수 있어
                            # 1이 된다 ex) 8 7 6 경우 6은 8을 볼 수 없음

print(cnt)