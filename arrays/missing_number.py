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
        
# Using XOR approach - but only finds one missing number, not multiple missing numbers!
nums = [1, 2, 3, 5]

def xor_approach(nums):
    xor = 0
    for i in range(1, max(nums)+1):
        xor ^= i
        
    for item in nums:
        xor ^= item
    
    return xor
            
print(xor_approach(nums))

arr = [1, 9, 7, 2, 5, 6]

items = set(arr)
missing_num = []
for i in range(1, max(items)+1):
    if i not in items:
        missing_num.append(i)
print(missing_num)