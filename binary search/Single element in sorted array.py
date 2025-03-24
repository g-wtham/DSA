arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

def singleElementInSortedArr(arr):
    low = 1
    n = len(arr)
    high = n-2

    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]

    while low <= high:
        mid = (low+high)//2
        
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:              # Middle element not equal to previous and next element, return arr[mid]
            return arr[mid]
        
        if (mid%2 == 0 and arr[mid] == arr[mid+1]) or (mid%2==1 and arr[mid] == arr[mid-1]):      # Left half condition
            low = mid+1
        else:
            high = mid-1

    return -1


print(singleElementInSortedArr(arr))

'''
1. Using low as 1 and high as n-1 , since, the edge cases are already handled, so checking 0th and n-1 is redundant, as the single element wont be present here.
2. Checks first and second element; Checks last and last before element; 
3. In this kinda problems, there is a PATTERN :
        (even, odd) -> pairs before SINGLE ELEMENT APPEARS, 
        (odd, even) -> pairs after SINGLE ELEMENT APPEARS, 
        
        [0,    1,  2,  3,     4] => Index

        [1,    1,  2,  3,     3] => Elements with duplicates
        [even,odd, _, odd, even] 

4. If mid is at EVEN position, then check if odd element, which should be at NEXT position is same or not. mid == mid+1
   If its same, then condition is satisfied, the single element wont be in this half, it will be in another half

5. For (odd, even) => mid%2 == 1 AND arr[mid] == arr[mid+1] or mid%2 == 0 AND arr[mid] == arr[mid-1]

'''