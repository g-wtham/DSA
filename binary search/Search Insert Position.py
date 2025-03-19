def lowerBound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)
    
    while left <= right:
        mid = (left+right)//2
        if arr[mid] >= target:
            ans = mid
            right = mid-1
        else:
            left = mid+1
    
    arr.append(0)
    for i in range(len(arr)-1, ans, -1):
        arr[i] = arr[i-1]
    arr[ans] = target   

    return arr

print(lowerBound([1,2,4,7], 3))