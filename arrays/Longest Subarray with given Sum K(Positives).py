k = 8
array = [2,3,5]
n = len(array)

def longest_subarray(n, k):
    max_length = 0
    for i in range(n):
        for j in range(i, n): # to generate all possible combos we need to iterate till n not just till i, as it will not consider every possible combo
            subarray = array[i:j+1] # as slicing is exclusive at `end`, add 1 & also array[0:0] is wrong, array[0:1] correctly slices the array!
        
            if sum(subarray) == k:   
                max_length = max(max_length, len(subarray))
        
    return max_length

print(longest_subarray(n, k))