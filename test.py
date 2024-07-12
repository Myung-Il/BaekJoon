n = int(input())

ans = 0
stack = []
# stack 의 추가 되는 수는 튜플형식(a.b) 인데, a 는 수를 나타내고, b는 앞자리까지의 영향력을 나타낸다.
for _ in range(n):
    h = int(input())
    # 스택의 제일 끝자리 보다 큰수가 들어왔을 시, stack[-1] 수의 앞자리 영향력을 더해준다.
    while stack and stack[-1][0] < h:
        ans += stack.pop()[1]

    if stack and stack[-1][0] == h:
        cnt = stack.pop()[1]
        ans += cnt
        # len(stack) 이 0 이 아니라면, stack 에 수가 들어왔을시,stack[-1]과 새로운 수의 관계를 더해준다.
        if len(stack) != 0:
            ans += 1 
        stack.append((h, cnt+1))
    else:
        # len(stack) 이 0 이 아니라면, stack 에 수가 들어왔을시,stack[-1]과 새로운 수의 관계를 더해준다.
        if len(stack) != 0:
            ans += 1
        stack.append((h, 1))

print(ans)

'''

7
2
4
1
2
2
5
1

          0
  0       0
  0       0
0 0   0 0 0
0 0 0 0 0 0 0
2 4 1 2 2 5 1
2 = 0 = 0
4 = 0+1 = 1
4 1 = 1+1 = 2
4 2 = 2+1+1 = 4
4 2 2 = 4+2 = 6
5 = 6+3 = 9
5 1 = 9+1 = 10

2 4 1 2 2 5 1
0 0 1 1 2 0 1 = 5
0 1 0 1 0 3 0 = 5

5 5 1 2 5
5 = 0 = 0
5 5 = 0+1 = 1
5 5 1 = 1+1 = 2
5 5 2 = 2+1+1 = 4
5 5 5 = 4+2+1 = 7

6
10
1
2
3
4
5
10 1 2 3 4 5
 0 1 1 1 1 1
 0 0 1 1 1 1

'''