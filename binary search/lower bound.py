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
            
    return ans

print(lowerBound([-1,12], 13))

'''
ans = len(arr) - as if target is greater than all elements found in our array. we keep storing mid value in ans variable
if arr[mid] is greater than target, we found a potential index position, but we need smallest number which is >= to the target, so move left side.
Because, if you move right, elements greater than target only exists, which we dont need, we only need elements which are greater than target but not the greatest, 
so we keep moving left side till high crosses low, which means low is at its lowest position, and high moves past this leads to -1 index, which is out of bounds.

We keep moving left (by setting high = mid - 1) to check if there are any other valid elements with smaller indices. 
This ensures we find the true lower bound - the first/smallest index where the element is greater than or equal to the target.
'''