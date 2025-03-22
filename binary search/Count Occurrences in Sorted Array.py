def countFreq(arr, target):
    def firstOccur(arr, target):
        first = -1
        low = 0
        high = len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid] >= target:
                if arr[mid] == target:
                    first = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return first
    
    def lastOccur(arr, target):
        last = -1
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] <= target:
                if arr[mid] == target:
                    last = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return last

    first, last = firstOccur(arr, target), lastOccur(arr, target)
    if first == -1 or last == -1:
        return 0
    return last - first + 1

arr= [1, 1, 2, 2, 2, 2, 3]
target = 1

print(countFreq(arr, target))

'''
If found element is equal, we assign it to the first variable,
If it's smaller, we increment low by 1 to focus on next half,
    i.e. divide search space by half and eliminate low values part
Thus, effectively we are moving rightwards even if we found the actual target, so we will have last occurence

Inversely, from the firstOccur function, we will get the first occurence, as we move leftwards from our found target value, 
so even if it's equal we will end up finding the first value.
'''