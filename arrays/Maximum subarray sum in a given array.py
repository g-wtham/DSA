arr = [-2,1,-3,4,-1,2,1,-5,4]

max_count = -float('inf')
count = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        subarray = arr[i:j+1]
        summ = sum(subarray)
        
        if summ > max_count:
            max_count = summ
            final_subarray = subarray
            
print(max_count, final_subarray)