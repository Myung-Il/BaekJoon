from sys import stdin
input=lambda:stdin.readline().rstrip()


def merge(arr):
    global res
    if len(arr)<2:return arr

    mid = len(arr)//2
    left_arr  = merge(arr[:mid])
    right_arr = merge(arr[mid:])

    merge_arr = []
    l, r = 0, 0
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            merge_arr.append(left_arr[l])
            l += 1
        else:
            merge_arr.append(right_arr[r])
            r += 1
            res += len(left_arr)-l
    
    merge_arr += left_arr[l:]
    merge_arr += right_arr[r:]
    return merge_arr


res = 0
n = int(input())
merge(list(map(int,input().split())))
print(res)