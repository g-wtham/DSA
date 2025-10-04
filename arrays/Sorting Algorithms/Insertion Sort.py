def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i-1   # previous pointer
        
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = current  

    return arr
        
print(insertion_sort([2,1]))

# %%

# Two parts - Sorted & Unsorted
arr = [3, 5, 1, 7, 8, 9]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_ele = arr[i]
        previous_index = i - 1

        while (arr[previous_index] > current_ele and previous_index >= 0):
            arr[previous_index + 1] = arr[previous_index]
            previous_index -= 1
            
        arr[previous_index + 1] = current_ele
        
    return arr

print(insertion_sort(arr))
        