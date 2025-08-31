nums = [-1,0,1,2,-1,-4]

nums.sort()
for i in range(len(nums)):
    left = i+1
    right = len(nums)-1
    while left < right:
        current_element = nums[i]
        
        three_sum = current_element + nums[left] + nums[right]
        
        if three_sum == 0:
            print(current_element, nums[left], nums[right])
            left += 1
            right -= 1
        elif three_sum > 0:  # means then higher values are added, so we need to reduce it, how ? reduce right index by 1
            right -= 1
        else:
            left += 1
