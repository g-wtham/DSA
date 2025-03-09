#Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1.

target=13
arr = [3,4,13,13,13,20,40]

left = 0
right = len(arr)
result = -1

while left <= right:
    mid = (left+right) // 2
    if arr[mid] == target:
        result = mid
        left = mid + 1
        
    elif arr[mid] < target:
        left = mid + 1
        
    else:
        right = mid - 1
        
print(result)