arr = [1, 2, 3, 4, 5]
k = 3

def max_subarray_with_size(arr, k):    
    window_size_sum = sum(arr[:k])   # Initial
    max_sum = window_size_sum
    start = 0
    end = k-1
    
    for i in range(k, len(arr)):
        window_size_sum = window_size_sum - arr[i-k] + arr[i]

        if window_size_sum > max_sum:
            max_sum = window_size_sum
            start = i-k+1
            end = i
        
    return max_sum, arr[start: end+1]

print(max_subarray_with_size(arr, k))
    
    
    