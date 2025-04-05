for _ in range(int(input())):
    n, m = map(int,input().split())
    for _ in  range(m):input()
    print(n-1)

# 비행기를 몇번 타느냐가 아닌
# 몇개의 비행기를 타느냐다
# 다음 정점에 가기 위해서는 비행기를 타야한다
# 한마디로 이미간 정점은 다시 갈 필요가 없다 어차피 돌아서 비행기를 탄다고 해도
# 비행기도 아직 안 타본 비행기일 것이기 때문이다