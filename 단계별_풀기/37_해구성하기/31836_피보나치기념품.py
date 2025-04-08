n = int(input())

fibo = [0, 1, 1]
for idx in range(2, n):
    fibo.append(fibo[idx]+fibo[idx-1])

    print(fibo)