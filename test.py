import sys

while True:
    n, *l = list(map(int, sys.stdin.readline().split()))
    if n == 0:break

    stack = []
    answer = 0

    for i in range(n):
        while stack and l[stack[-1]] > l[i]:     # 스택이 쌓여있고 이전 값보다 작아졌다면 실행
            tmp = stack.pop()                    # 스택의 마지막 값 출력

            if len(stack) == 0:                  # 만일 스택이 쌓여있지 않다면
                width = i                        # 너비를 지금까지의 거리로 지정
            else:                                # 그렇지 않다면
                width = i - stack[-1] - 1        # 
            answer = max(answer, width * l[tmp])
        stack.append(i)

        print(stack)
    while stack:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        answer = max(answer, width * l[tmp])

    print(answer)