import math

def angle(ax, ay, bx, by, cx, cy):
    bax, bay = ax-bx, ay-by # 벡터 BA
    bcx, bcy = cx-bx, cy-by # 벡터 BC

    # 내적과 외적
    dot = bax*bcx + bay*bcy
    det = bax*bcy - bay*bcx

    theta_rad = math.atan2(-det, dot)
    theta_deg = math.degrees(theta_rad)
    return theta_deg % 360

a = -1, 0
b = 0, 0
c = 1, 2

print(angle(*a, *b, *c))