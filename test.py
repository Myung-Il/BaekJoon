def verticality(x1, y1, x2, y2, x3, y3):
    numerator = abs((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 - y2*x1)
    denominator = ((y2-y1)**2 + (x2-x1)**2)**0.5
    return numerator / denominator

def horizontal(x1, y1, x2, y2, x3, y3):
    t = ((x3-x1)*(x2-x1) + (y3-y1)*(y2-y1)) / ((x2-x1)**2 + (y2-y1)**2)
    return (x1 + t*(x2-x1), y1 + t*(y2-y1))

def horizontal1(x1, y1, xD, yD):
    return ((xD-x1)**2 + (yD-y1)**2)**0.5

# 예시 사용법
A = (0, 0)
B = (1, 0)
C = (-2, -1)

# 직선 AB에 수직인 점 C에서 D까지의 최단 거리
D = horizontal(*A, *B, *C)
distance = horizontal1(*A, *D)
print(f"점 A에서 점 D까지의 거리: {distance}")