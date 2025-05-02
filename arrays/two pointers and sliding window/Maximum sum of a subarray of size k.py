arr = [-1, 2, 3,3,4,5,-1]

def subarray_sum(arr, k):
    left = 0
    right = k-1
    max_sum = 0       
    while right < len(arr)-1:
        sub_sum = 0 
        for i in range(left, right):
            sub_sum += arr[i]
            
        sub_sum -= arr[left]
        left += 1
        right += 1
        sub_sum += arr[right]
        
        max_sum = max(max_sum, sub_sum)
        
    return max_sum

print(subarray_sum(arr, 4))