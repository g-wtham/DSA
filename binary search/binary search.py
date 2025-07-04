def search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high = mid-1
    
    return -1

print(search([-1,0,3,5,9,12], 5))