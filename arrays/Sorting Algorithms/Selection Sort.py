def selection_sort(arr):
    for i in range(len(arr)):
        step = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[step]:
                step = j
        arr[step], arr[i] = arr[i], arr[step]
        
    return arr
print(selection_sort([2,1,4,6,3]))

# %%
arr = [3, 5, 1, 7, 8, 9]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr
    
print(selection_sort(arr))       
    