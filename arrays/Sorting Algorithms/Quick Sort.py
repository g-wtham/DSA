def quicksort(arr, low, high):
    if (low < high):
        partitionIndex = partition(arr, low, high)
        quicksort(arr, low, partitionIndex-1)
        quicksort(arr, partitionIndex+1, high)
        
    return arr
        
def partition(arr, low, high):
    pivot_element = arr[low]
    i = low
    j = high
    
    while (i < j):
        
        while (arr[i] <= pivot_element and i <= high-1):
            i += 1
            
        while (arr[j] > pivot_element and j >= low + 1):
            j -= 1
            
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[low], arr[j] = arr[j], arr[low]
    
    return j
            
arr = [3, 5, 1, 7, 8, 9]     
print(quicksort(arr, 0, len(arr)-1))