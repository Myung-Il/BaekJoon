from sys import stdin
input = lambda:stdin.readline().strip()

n = int(input())
x, y = map(int, input().split())
cx, cy = x-1, 2**n-y

tiles = [[0]*2**n for _ in range(2**n)]
tiles[cy][cx] = -1

num = 1
def site(t, point, left, right, bottom, top):
    global num

    if left+1==right and bottom+1==top:
        if point!=(right, bottom):t[bottom][right] = num
        if point!=(left,  bottom):t[bottom][left ] = num
        if point!=(left,  top   ):t[top   ][left ] = num
        if point!=(right, top   ):t[top   ][right] = num
    
    else:
        midx = (left+right)//2
        midy = (bottom+top)//2

        nx, ny = point
        site(t, point if midx+1<=nx<=right and bottom<=ny<=midy else(midx+1, midy),   midx+1, right, bottom, midy);num+=1
        site(t, point if left<=nx<=midx    and bottom<=ny<=midy else(midx,   midy),   left,   midx,  bottom, midy);num+=1
        site(t, point if left<=nx<=midx    and midy+1<=ny<=top  else(midx,   midy+1), left,   midx,  midy+1, top );num+=1
        site(t, point if midx+1<=nx<=right and midy+1<=ny<=top  else(midx+1, midy+1), midx+1, right, midy+1, top );num+=1

        if not t[ midy ][midx+1]:t[ midy ][midx+1] = num
        if not t[ midy ][ midx ]:t[ midy ][ midx ] = num
        if not t[midy+1][ midx ]:t[midy+1][ midx ] = num
        if not t[midy+1][midx+1]:t[midy+1][midx+1] = num
        num+=1

site(tiles, (cx, cy), 0, 2**n-1, 0, 2**n-1)
for tl in tiles:print(*tl)