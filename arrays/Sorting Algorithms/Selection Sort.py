def selection_sort(arr):
    for i in range(len(arr)):
        step = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[step]:
                step = j
        arr[step], arr[i] = arr[i], arr[step]
        
    return arr
print(selection_sort([2,1,4,6,3]))