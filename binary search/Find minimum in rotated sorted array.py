arr = [4,5,6,7,0,1,2,3]
import sys
def minSortedArray(arr):
    low = 0
    high = len(arr)-1
    minEle = sys.maxsize
    while low <= high:
        mid = (low+high)//2
        if arr[mid] <= minEle:
            return arr[mid]
        if arr[low] <= arr[mid]:
            minEle = min(minEle, arr[low])
            low = mid+1
        else:
            minEle = min(minEle, arr[mid])
            high = mid-1
                
    return minEle

print(minSortedArray(arr))
