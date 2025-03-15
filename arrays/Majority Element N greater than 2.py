def majorityElement(nums):

    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1
        
        if count > len(nums)//2:
            return nums[i], count
        
print(majorityElement([2,2,1,1,1,2,2]))

# Optimal Approach:

def majorityElementOptimal(nums):
    candidate = nums[0]
    count = 0
    
    for i in range(len(nums)):
        if nums[i] == candidate:
            count += 1
        if count == 0:
            candidate = nums[i]
        else:
            count -= 1
            
    return candidate

print(majorityElementOptimal([2,2,1,1,1,2,2]))

'''
Boyer-Moore Voting Algorithm :
- How does it work?
    Pick a candidate (start with the first element).
    Use a count variable:
    Increase count if the current element is the same as the candidate.
    Decrease count if the current element is different.
    If the count becomes 0, change the candidate to the current element.
    At the end, the remaining candidate is the majority element.
- Why does it work?
    Since the majority element appears more than half the time, all other elements combined cannot cancel it out.
    So, the last remaining candidate is the correct answer.
'''