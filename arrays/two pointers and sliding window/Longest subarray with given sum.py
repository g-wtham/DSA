arr = [2,5,1,10,10]
k = 14

# window size = 1

l, r = 0, 0
maximum_len = 0
sum = 0
while r < len(arr):
    sum += arr[r]
    
    if sum <= k:
        maximum_len = max(maximum_len, r-l+1)
        
    while sum > k:
        sum -= arr[l]
        l+=1
        
    r += 1
    
print(maximum_len)    
    