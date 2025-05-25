def selection_sort(arr):
    for i in range(len(arr)):
        step = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[step]:
                min = j
        arr[step], arr[min] = arr[min], arr[step]
        
    return arr
print(selection_sort([2,1,4,6,3]))