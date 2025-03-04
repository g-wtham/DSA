nums = [2, 7, 11, 15]
target = 26
list1 = []
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == target:
            list1.append(i)
            list1.append(j)
    
print(list1)        