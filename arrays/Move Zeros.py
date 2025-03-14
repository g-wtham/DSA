arr = [0, 1, 0, 1,0,1,0, 1, 1]

count_0 = 0
count_1 = 0
for item in arr:
    if item == 0:
        count_0 += 1
    elif item == 1:
        count_1 += 1
        
for i in range(count_0):
    arr[i] = 0
    
for i in range(count_0, len(arr)):
    arr[i] = 1
    
print(arr)