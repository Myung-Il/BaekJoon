def mergeSort(arr):
    global result
    if len(arr) < 2: return arr

    mid = len(arr)//2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    merge_arr = []
    l = r = 0
    while l < len(left) and r < len(right):
        if(left[l] <= right[r]):
            merge_arr.append(left[l])
            l += 1
        else:
            merge_arr.append(right[r])
            r += 1
            result += len(left)-l

    merge_arr += left[l:]
    merge_arr += right[r:]
    return merge_arr

import sys
input = sys.stdin.readline

result = 0
N = input()
array = list(map(int, input().split()))

mergeSort(array)
print(result)