def height(x1, y1, x2, y2, px, py):
    ax, ay = px - x1, py - y1
    bx, by = x2 - x1, y2 - y1

    cross = abs(ax*by - ay*bx)
    base = ((bx)**2 + (by)**2)**0.5
    return cross/base


a = 0, 0
b = 1, 1
print(height(*a, *b, 0, 2))