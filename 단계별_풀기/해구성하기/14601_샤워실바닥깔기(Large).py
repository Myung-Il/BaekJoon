from sys import stdin
input = lambda:stdin.readline().strip()


def print_tiles(t):
    """주어진 2D 리스트(타일)를 오른쪽 3칸 정렬하여 출력합니다."""
    for row in t:
        output_line = ""
        for num in row:
            # -1은 'X'로 표시하고, 3칸 오른쪽 정렬
            display_char = 'X' if num == -1 else str(num)
            output_line += f"{display_char:>3}"
        print(output_line)
'''
1
1 1
= 1 1
= X 1

2
3 2
= 4 4 5 5
= 4 3 3 5
= 1 3 X 2
= 1 1 2 2


8 8 9 9  0 0 1 1
8 6 6 9  0 7 7 1
2 6 3 3  4 4 7 5
2 2 3 0  0 4 5 5

7 7 8 0  9 9 1 1
7 5 8 8  9 6 6 1
1 5 5 2  X 3 6 4
1 1 2 2  3 3 4 4
'''

n = int(input())
x, y = map(int, input().split())
cx, cy = x-1, 2**n-y

tiles = [[0]*2**n for _ in range(2**n)]
tiles[cy][cx] = -1

num = 1
def tileSet(t, size, dir, left, right, bottom, top):
    global num

    if size==2:
        if t[top][left]==-1:t[bottom][right] = num
        elif not t[top][left] and dir!=1:t[top][left] = num

        if t[top][right]==-1:t[bottom][left] = num
        elif not t[top][right] and dir!=2:t[top][right] = num

        if t[bottom][left]==-1:t[top][right] = num
        elif not t[bottom][left] and dir!=4:t[bottom][left] = num

        if t[bottom][right]==-1:t[top][left] = num
        elif not t[bottom][right] and dir!=3:t[bottom][right] = num
        num+=1
    elif size>2:
        midr = (left+right)//2
        midc = (bottom+top)//2

        tileSet(t, size//2, 2, left, midr, bottom, midc)
        tileSet(t, size//2, 1, midr+1, right, bottom, midc)
        tileSet(t, size//2, 3, left, midr, midc+1, top)
        tileSet(t, size//2, 4, midr+1, right, midc+1, top)

        if midr>cx or cx>midr+1 or midc>cy or cy>midc+1:
            if dir==1:
                t[midc+1][ midr ] = t[midc+2][midr-1]
                t[midc+2][midr-1] = 0
            if dir==2:
                t[midc+1][midr+1] = t[midc+2][midr+2]
                t[midc+2][midr+2] = 0
            if dir==3:
                t[ midc ][midr+1] = t[midc-1][midr+2]
                t[midc-2][midr+2] = 0
            if dir==4:
                t[ midc ][ midr ] = t[midc-1][midr-1]
                t[midc-1][midr-1] = 0

        if not t[ midc ][ midr ]:t[ midc ][ midr ] = num
        if not t[midc+1][ midr ]:t[midc+1][ midr ] = num
        if not t[ midc ][midr+1]:t[ midc ][midr+1] = num
        if not t[midc+1][midr+1]:t[midc+1][midr+1] = num
        num+=1
        
    print_tiles(t)
    print("="*(2**n*3+1))

if 2**(n-1)<cx and 2**(n-1)>=cy:dir = 1
if 2**(n-1)>=cx and 2**(n-1)>=cy:dir = 2
if 2**(n-1)>=cx and 2**(n-1)<cy:dir = 3
if 2**(n-1)<cx and 2**(n-1)<cy:dir = 4
tileSet(tiles, 2**n, 0, 0, 2**n-1, 0, 2**n-1)
for row in tiles:
    output_line = ""
    for num in row:output_line += f"{num:>3}"
    print(output_line)