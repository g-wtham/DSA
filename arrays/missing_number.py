arr = [1, 2, 5, 6, 9]

total_n = max(arr)

for i in range(1, total_n+1):
    found = False
    for j in range(len(arr)):
        if arr[j] == i:
            found = True
            break
            
    if not found:
        print(i)