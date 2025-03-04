arr = [1, 7, 2, 5, 6, 9]

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[j] < arr[i]:
            count += 1
            
    print("Smaller than", arr[i], " = ", count)