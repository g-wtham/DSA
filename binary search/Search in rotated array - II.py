arr = [3, 8, 1, 2, 3, 3, 3, 4, 5, 3]
k = 5

def searchRotated(arr, k):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            return True
        if arr[low] == arr[mid] == arr[high]:  # Shrink search space
            low+=1
            high-=1
        if arr[low] <= arr[mid]:
            if arr[low] <= k <= arr[mid]:
                high = mid-1
            else:
                low = mid + 1
        else:
            if arr[mid] <= arr[high]:
                if arr[mid] <= k <= arr[high]:
                    low = mid + 1
                else:
                    high = mid-1               
            
    return False

print(searchRotated(arr, k))

'''
In questions where there are duplicate elements, what we have to do is to check the lowest middle and last element,
whether they are same or not, Since when we are dividing the search space, 
we have the high chances that the elements which are going to be in one partwhether left side or right side, 
gonna meet with this condition of having the lowest value and middle value being equal. 
So if its equal, we need to decrement high value and increment lower value, which means we are reducing or shrinking the search space
'''