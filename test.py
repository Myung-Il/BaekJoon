l = [1, 2, 3]

def f(arr, result, idx, sum):
    if len(arr)==idx:
        result.append(sum)
        return result
    
    f(arr, result, idx+1, sum)
    f(arr, result, idx+1, sum+arr[idx])
    return result

print(sorted(f(l, [], 0, 0)))