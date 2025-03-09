#Given a sorted array of N integers, write a program to find the index of the last occurrence of the target key. If the target is not found then return -1.

target=13
arr = [3,4,13,13,13,20,40]

def last_occur(target, arr):
    left = 0
    right = len(arr)
    result1 = -1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            result1 = mid
            left = mid + 1
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    return result1


def first_occur(target, arr):
    left = 0
    right = len(arr)
    result2 = -1

    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == target:
            result2 = mid
            right = mid - 1
        
        elif arr[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    return result2

last_occur = last_occur(target, arr)
first_occur = first_occur(target, arr)

        
print("Target", target, "first occurs at index", first_occur, "and last occurs at index", last_occur)