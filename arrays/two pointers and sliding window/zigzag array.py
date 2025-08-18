arr = [4, 3, 7, 8, 6, 2, 1]

for i in range(len(arr)-1):
    if i % 2 == 0:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    else:
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            
print(arr)