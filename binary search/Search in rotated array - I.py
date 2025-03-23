arr = [4,5,6,7,0,1,2,3]
k = 3

'''
1. Find unsorted part
2. Eliminate unsorted part, search in sorted part
3. Condition to check if its sorted or not -> 
        LEFT PART : element at low <= target <= element at mid
        RIGHT PART : element at mid <= target <= element at high
4. If the condition fails, 
        If left is unsorted, make LOW = MID + 1, eliminating left part, moving to the sorted part

KEY THING : If array is rotated at some position, then there are 2 parts: UNSORTED and SORTED part for sure
            So, if one part is UNSORTED, then there is SORTED part at other end
5. 
'''

def searchRotated(arr, k):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            return mid
        elif arr[low] <= k <= arr[mid]:
            high = mid-1
        else:
            low = mid+1
            
    return mid

print(searchRotated(arr, k))
            
    